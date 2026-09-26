"""2. CRIPTOGRAFIA CLASICA.

Cifrados y sustituciones del taller. Cada algoritmo es una funcion
independiente que recibe el texto y los parametros del cifrado, y
devuelve un diccionario con el texto original y el resultado.
"""

import math

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFABETO_27 = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

VALORES_AFIN = "1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23 y 25"


def _validar_modo(modo: str) -> str:
    modo = modo.upper()

    if modo not in ("C", "D"):
        raise ValueError("Opción no válida.")

    return modo


def modulo_27(texto: str, desplazamiento: int) -> dict:
    """2.1 Cifrado sobre un alfabeto de 27 simbolos (espacio + A-Z)."""
    mayusculas = texto.upper()

    resultado = ""

    for caracter in mayusculas:
        if caracter in ALFABETO_27:
            posicion = ALFABETO_27.index(caracter)
            resultado += ALFABETO_27[(posicion + desplazamiento) % 27]
        else:
            resultado += caracter

    return {
        "texto": texto,
        "alfabeto": mayusculas,
        "desplazamiento": desplazamiento,
        "resultado": resultado,
    }


def cesar(texto: str, desplazamiento: int, descifrar: bool = False) -> dict:
    """2.2 Cifrado Cesar. Descifrar equivale a desplazar en negativo."""
    if descifrar:
        desplazamiento = -desplazamiento

    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            inicio = ord("A") if caracter.isupper() else ord("a")
            nueva_letra = chr(
                (ord(caracter) - inicio + desplazamiento) % 26 + inicio
            )
            resultado += nueva_letra
        else:
            resultado += caracter

    return {
        "texto": texto,
        "desplazamiento": desplazamiento,
        "modo": "descifrar" if descifrar else "cifrar",
        "resultado": resultado,
    }


def vernam(texto: str, clave: str) -> dict:
    """2.3 Cifrado Vernam. La clave debe tener el mismo largo que el texto."""
    texto = texto.upper()
    clave = clave.upper()

    if len(texto) != len(clave):
        raise ValueError(
            "Error: el texto y la clave deben tener la misma longitud."
        )

    resultado = ""

    for letra_texto, letra_clave in zip(texto, clave):
        if letra_texto.isalpha() and letra_clave.isalpha():
            valor_texto = ord(letra_texto) - ord("A")
            valor_clave = ord(letra_clave) - ord("A")

            valor_resultado = valor_texto ^ valor_clave
            valor_resultado %= 26

            resultado += chr(valor_resultado + ord("A"))
        else:
            resultado += letra_texto

    return {
        "texto": texto,
        "clave": clave,
        "resultado": resultado,
    }


def atbash(texto: str) -> dict:
    """2.4 Cifrado Atbash: A<->Z, B<->Y, C<->X..."""
    resultado = ""

    for caracter in texto:
        if caracter.isupper():
            resultado += chr(ord("Z") - (ord(caracter) - ord("A")))
        elif caracter.islower():
            resultado += chr(ord("z") - (ord(caracter) - ord("a")))
        else:
            resultado += caracter

    return {
        "texto": texto,
        "resultado": resultado,
    }


def transposicion_columnar(texto: str, clave: str) -> dict:
    """2.5 Transposicion columnar con clave.

    El numero de columnas es la cantidad de letras de la clave y las
    columnas se leen segun el orden alfabetico de esas letras, no de
    izquierda a derecha. La clave no puede repetir letras porque eso
    haria ambigua la lectura.
    """
    clave = clave.upper()

    if len(clave) < 2:
        raise ValueError(
            "Error: la clave debe tener al menos 2 letras."
        )

    if not clave.isalpha():
        raise ValueError("Error: la clave solo debe contener letras.")

    if len(set(clave)) != len(clave):
        raise ValueError(
            "Error: la clave no puede tener letras repetidas."
        )

    columnas = len(clave)
    limpio = texto.replace(" ", "")

    relleno = limpio

    while len(relleno) % columnas != 0:
        relleno += "X"

    filas = len(relleno) // columnas
    matriz = []

    for i in range(filas):
        fila = {}

        for j in range(columnas):
            fila[clave[j]] = relleno[i * columnas + j]

        matriz.append(fila)

    orden = sorted(range(columnas), key=lambda j: clave[j])
    resultado = ""

    for j in orden:
        for i in range(filas):
            resultado += matriz[i][clave[j]]

    return {
        "texto": texto,
        "clave": clave,
        "columnas": columnas,
        "filas": filas,
        "orden_lectura": [f"{j + 1}:{clave[j]}" for j in orden],
        "matriz": matriz,
        "texto_relleno": relleno,
        "resultado": resultado,
    }


def afin(texto: str, a: int, b: int, modo: str = "C") -> dict:
    """2.6 Cifrado afin y = (a * x + b) mod 26."""
    if math.gcd(a, 26) != 1:
        raise ValueError(
            "Error: 'a' debe ser coprimo con 26.\n"
            f"Valores posibles: {VALORES_AFIN}."
        )

    modo = _validar_modo(modo)
    mayusculas = texto.upper()
    resultado = ""

    if modo == "C":
        for caracter in mayusculas:
            if caracter.isalpha():
                x = ord(caracter) - ord("A")
                y = (a * x + b) % 26
                resultado += chr(y + ord("A"))
            else:
                resultado += caracter
    else:
        inverso_a = pow(a, -1, 26)

        for caracter in mayusculas:
            if caracter.isalpha():
                y = ord(caracter) - ord("A")
                x = (inverso_a * (y - b)) % 26
                resultado += chr(x + ord("A"))
            else:
                resultado += caracter

    return {
        "texto": texto,
        "alfabeto": mayusculas,
        "a": a,
        "b": b,
        "modo": "cifrar" if modo == "C" else "descifrar",
        "resultado": resultado,
    }


def sustitucion_simple(texto: str, clave: str, modo: str = "C") -> dict:
    """2.7 Cifra de sustitucion simple con un alfabeto de 26 letras."""
    clave = clave.upper()

    if len(clave) != 26:
        raise ValueError(
            "Error: la clave debe tener exactamente 26 letras."
        )

    if not clave.isalpha():
        raise ValueError("Error: la clave solo debe contener letras.")

    if len(set(clave)) != 26:
        raise ValueError("Error: no puede haber letras repetidas.")

    modo = _validar_modo(modo)
    resultado = ""

    if modo == "C":
        for caracter in texto:
            if caracter.upper() in ALFABETO:
                posicion = ALFABETO.index(caracter.upper())
                nueva_letra = clave[posicion]

                if caracter.islower():
                    nueva_letra = nueva_letra.lower()

                resultado += nueva_letra
            else:
                resultado += caracter
    else:
        for caracter in texto:
            if caracter.upper() in clave:
                posicion = clave.index(caracter.upper())
                nueva_letra = ALFABETO[posicion]

                if caracter.islower():
                    nueva_letra = nueva_letra.lower()

                resultado += nueva_letra
            else:
                resultado += caracter

    return {
        "texto": texto,
        "clave": clave,
        "modo": "cifrar" if modo == "C" else "descifrar",
        "resultado": resultado,
    }
