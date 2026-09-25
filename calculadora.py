
import math
import hashlib
import base64
import secrets
import string


# ============================================================
#                 FUNCIONES AUXILIARES
# ============================================================

def pausar():
    input("\nPresione ENTER para continuar...")


def limpiar_texto(texto):
    return texto.upper()


# ============================================================
#              1. MATEMÁTICA MODULAR
# ============================================================

def calcular_modulo():
    print("\n--- 1.1 CALCULAR MÓDULO ---")

    try:
        a = int(input("Ingrese el valor de a: "))
        n = int(input("Ingrese el valor de n: "))

        if n == 0:
            print("Error: el módulo n no puede ser 0.")
            return

        resultado = a % n

        print(f"\n{a} mod {n} = {resultado}")

    except ValueError:
        print("Error: debe ingresar números enteros.")


def inverso_aditivo():
    print("\n--- 1.2 INVERSO ADITIVO ---")

    try:
        a = int(input("Ingrese el valor de a: "))
        n = int(input("Ingrese el módulo n: "))

        if n <= 0:
            print("Error: el módulo debe ser mayor que 0.")
            return

        resultado = (-a) % n

        print(f"\nEl inverso aditivo de {a} módulo {n} es: {resultado}")
        print(
            f"Comprobación: ({a} + {resultado}) mod {n} = "
            f"{(a + resultado) % n}"
        )

    except ValueError:
        print("Error: debe ingresar números enteros.")


def inverso_xor():
    print("\n--- 1.3 INVERSO DE XOR ---")

    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

        resultado = a ^ b

        print(f"\n{a} XOR {b} = {resultado}")

        comprobacion = resultado ^ b

        print(f"Comprobación: {resultado} XOR {b} = {comprobacion}")

    except ValueError:
        print("Error: debe ingresar números enteros.")


def calcular_mcd():
    print("\n--- 1.4 MCD E INVERSO MULTIPLICATIVO ---")

    try:
        a = int(input("Ingrese el valor de a: "))
        n = int(input("Ingrese el módulo n: "))

        if n <= 0:
            print("Error: el módulo debe ser mayor que 0.")
            return

        mcd = math.gcd(a, n)

        print(f"\nMCD({a}, {n}) = {mcd}")

        if mcd == 1:
            print("Sí existe inverso multiplicativo.")

            inverso = pow(a, -1, n)

            print(f"Inverso multiplicativo = {inverso}")
            print(
                f"Comprobación: ({a} × {inverso}) mod {n} = "
                f"{(a * inverso) % n}"
            )
        else:
            print("No existe inverso multiplicativo.")
            print("La razón es que MCD(a, n) ≠ 1.")

    except ValueError:
        print("Error: debe ingresar números enteros.")


def inverso_multiplicativo_tradicional():
    print("\n--- 1.5 INVERSO MULTIPLICATIVO - MÉTODO TRADICIONAL ---")

    try:
        a = int(input("Ingrese el valor de a: "))
        n = int(input("Ingrese el módulo n: "))

        if n <= 0:
            print("Error: el módulo debe ser mayor que 0.")
            return

        mcd = math.gcd(a, n)

        if mcd != 1:
            print(f"\nMCD({a}, {n}) = {mcd}")
            print("No existe inverso multiplicativo.")
            return

        print("\nBuscando x tal que:")
        print(f"{a} × x ≡ 1 (mod {n})")
        print("\nProcedimiento:")

        for x in range(1, n):
            resultado = (a * x) % n

            print(f"{a} × {x} mod {n} = {resultado}")

            if resultado == 1:
                print(f"\nInverso multiplicativo = {x}")
                print(
                    f"Comprobación: ({a} × {x}) mod {n} = "
                    f"{(a * x) % n}"
                )
                return

    except ValueError:
        print("Error: debe ingresar números enteros.")


def inverso_multiplicativo_aee():
    print("\n--- 1.6 INVERSO MULTIPLICATIVO - AEE ---")

    try:
        a = int(input("Ingrese el valor de a: "))
        n = int(input("Ingrese el módulo n: "))

        if n <= 0:
            print("Error: el módulo debe ser mayor que 0.")
            return

        # Guardamos los valores originales
        a_original = a
        n_original = n

        # Para trabajar correctamente
        if a < 0:
            a = a % n

        # Variables para el algoritmo extendido
        r0 = n
        r1 = a

        t0 = 0
        t1 = 1

        tabla = []

        while r1 != 0:
            cociente = r0 // r1
            residuo = r0 % r1

            tabla.append((r0, r1, cociente, residuo, t0, t1))

            r0, r1 = r1, residuo
            t0, t1 = t1, t0 - cociente * t1

        mcd = r0

        print(f"\nMCD({a_original}, {n_original}) = {mcd}")

        if mcd != 1:
            print("No existe inverso multiplicativo.")
            return

        inverso = t0 % n_original

        print(f"Rondas del algoritmo: {len(tabla)}")

        print("\nTABLA DEL ALGORITMO EXTENDIDO DE EUCLIDES")
        print("-" * 75)
        print(
            f"{'Ronda':<8}"
            f"{'r anterior':<15}"
            f"{'r actual':<15}"
            f"{'Cociente':<12}"
            f"{'Residuo':<12}"
        )
        print("-" * 75)

        for i, fila in enumerate(tabla, start=1):
            r_anterior, r_actual, cociente, residuo, _, _ = fila

            print(
                f"{i:<8}"
                f"{r_anterior:<15}"
                f"{r_actual:<15}"
                f"{cociente:<12}"
                f"{residuo:<12}"
            )

        print("-" * 75)

        print(f"\nInverso multiplicativo = {inverso}")

        print(
            f"Comprobación: ({a_original} × {inverso}) mod "
            f"{n_original} = "
            f"{(a_original * inverso) % n_original}"
        )

    except ValueError:
        print("Error: debe ingresar números enteros.")


# ============================================================
#              2. CRIPTOGRAFÍA CLÁSICA
# ============================================================

def modulo_27():
    print("\n--- 2.1 CIFRADO MÓDULO 27 ---")

    texto = input("Ingrese el texto: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))

    # Alfabeto de 27 símbolos: espacio + A-Z
    alfabeto = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resultado = ""

    for caracter in texto.upper():
        if caracter in alfabeto:
            posicion = alfabeto.index(caracter)
            nueva_posicion = (posicion + desplazamiento) % 27
            resultado += alfabeto[nueva_posicion]
        else:
            resultado += caracter

    print(f"\nTexto original: {texto}")
    print(f"Texto cifrado:  {resultado}")


def cesar():
    print("\n--- 2.2 CIFRADO CÉSAR ---")

    texto = input("Ingrese el texto: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))

    opcion = input("¿Desea cifrar o descifrar? (C/D): ").upper()

    if opcion == "D":
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

    print(f"\nResultado: {resultado}")


def vernam():
    print("\n--- 2.3 CIFRADO VERNAM ---")

    texto = input("Ingrese el texto: ").upper()
    clave = input("Ingrese la clave: ").upper()

    if len(texto) != len(clave):
        print("Error: el texto y la clave deben tener la misma longitud.")
        return

    resultado = ""

    for t, k in zip(texto, clave):
        if t.isalpha() and k.isalpha():
            valor_t = ord(t) - ord("A")
            valor_k = ord(k) - ord("A")

            valor_resultado = valor_t ^ valor_k

            # Se mantiene dentro de A-Z para mostrar el resultado
            valor_resultado %= 26

            resultado += chr(valor_resultado + ord("A"))
        else:
            resultado += t

    print(f"\nTexto:  {texto}")
    print(f"Clave:  {clave}")
    print(f"Resultado: {resultado}")


def atbash():
    print("\n--- 2.4 CIFRADO ATBASH ---")

    texto = input("Ingrese el texto: ")

    resultado = ""

    for caracter in texto:
        if caracter.isupper():
            resultado += chr(ord("Z") - (ord(caracter) - ord("A")))
        elif caracter.islower():
            resultado += chr(ord("z") - (ord(caracter) - ord("a")))
        else:
            resultado += caracter

    print(f"\nResultado: {resultado}")


def transposicion_columnar():
    print("\n--- 2.5 TRANSPOSICIÓN COLUMNAR SIMPLE ---")

    texto = input("Ingrese el texto: ").replace(" ", "")
    columnas = int(input("Ingrese el número de columnas: "))

    if columnas <= 0:
        print("Error: el número de columnas debe ser mayor que 0.")
        return

    # Completar con X para formar la matriz
    while len(texto) % columnas != 0:
        texto += "X"

    filas = len(texto) // columnas

    matriz = []

    for i in range(filas):
        fila = list(texto[i * columnas:(i + 1) * columnas])
        matriz.append(fila)

    print("\nMatriz:")

    for fila in matriz:
        print(" ".join(fila))

    resultado = ""

    for columna in range(columnas):
        for fila in range(filas):
            resultado += matriz[fila][columna]

    print(f"\nTexto cifrado: {resultado}")


def afin():
    print("\n--- 2.6 CIFRADO AFÍN ---")

    texto = input("Ingrese el texto: ")
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))

    if math.gcd(a, 26) != 1:
        print("Error: 'a' debe ser coprimo con 26.")
        print("Valores posibles: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23 y 25.")
        return

    opcion = input("¿Desea cifrar o descifrar? (C/D): ").upper()

    resultado = ""

    if opcion == "C":
        for caracter in texto.upper():
            if caracter.isalpha():
                x = ord(caracter) - ord("A")
                y = (a * x + b) % 26
                resultado += chr(y + ord("A"))
            else:
                resultado += caracter

    elif opcion == "D":
        inverso_a = pow(a, -1, 26)

        for caracter in texto.upper():
            if caracter.isalpha():
                y = ord(caracter) - ord("A")
                x = (inverso_a * (y - b)) % 26
                resultado += chr(x + ord("A"))
            else:
                resultado += caracter
    else:
        print("Opción no válida.")
        return

    print(f"\nResultado: {resultado}")


def sustitucion_simple():
    print("\n--- 2.7 CIFRA DE SUSTITUCIÓN SIMPLE ---")

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    clave = input(
        "Ingrese el alfabeto de sustitución (26 letras): "
    ).upper()

    if len(clave) != 26:
        print("Error: la clave debe tener exactamente 26 letras.")
        return

    if not clave.isalpha():
        print("Error: la clave solo debe contener letras.")
        return

    if len(set(clave)) != 26:
        print("Error: no puede haber letras repetidas.")
        return

    texto = input("Ingrese el texto: ")
    opcion = input("¿Desea cifrar o descifrar? (C/D): ").upper()

    resultado = ""

    if opcion == "C":
        for caracter in texto:
            if caracter.upper() in alfabeto:
                posicion = alfabeto.index(caracter.upper())
                nueva_letra = clave[posicion]

                if caracter.islower():
                    nueva_letra = nueva_letra.lower()

                resultado += nueva_letra
            else:
                resultado += caracter

    elif opcion == "D":
        for caracter in texto:
            if caracter.upper() in clave:
                posicion = clave.index(caracter.upper())
                nueva_letra = alfabeto[posicion]

                if caracter.islower():
                    nueva_letra = nueva_letra.lower()

                resultado += nueva_letra
            else:
                resultado += caracter
    else:
        print("Opción no válida.")
        return

    print(f"\nResultado: {resultado}")


# ============================================================
#              3. CRIPTOGRAFÍA MODERNA
# ============================================================

def diffie_hellman():
    print("\n--- 3.1 DIFFIE-HELLMAN ---")

    try:
        p = int(input("Ingrese un número primo p: "))
        g = int(input("Ingrese la raíz primitiva g: "))

        a = int(input("Ingrese la clave privada de Alice: "))
        b = int(input("Ingrese la clave privada de Bob: "))

        A = pow(g, a, p)
        B = pow(g, b, p)

        clave_alice = pow(B, a, p)
        clave_bob = pow(A, b, p)

        print("\n--- RESULTADOS ---")
        print(f"Clave pública de Alice: {A}")
        print(f"Clave pública de Bob:   {B}")
        print(f"Clave calculada por Alice: {clave_alice}")
        print(f"Clave calculada por Bob:   {clave_bob}")

        if clave_alice == clave_bob:
            print("\nIntercambio exitoso.")
            print(f"Clave compartida: {clave_alice}")

    except ValueError:
        print("Error: todos los valores deben ser números enteros.")


def rsa():
    print("\n--- 3.2 RSA ---")

    try:
        p = int(input("Ingrese el número primo p: "))
        q = int(input("Ingrese el número primo q: "))

        n = p * q
        phi = (p - 1) * (q - 1)

        print(f"\nn = p × q = {n}")
        print(f"φ(n) = {phi}")

        e = int(input("Ingrese e: "))

        if math.gcd(e, phi) != 1:
            print("Error: e debe ser coprimo con φ(n).")
            return

        d = pow(e, -1, phi)

        print(f"Clave pública: (e={e}, n={n})")
        print(f"Clave privada: (d={d}, n={n})")

        mensaje = int(input(f"Ingrese el mensaje como número menor que {n}: "))

        if mensaje < 0 or mensaje >= n:
            print("Error: el mensaje debe estar entre 0 y n-1.")
            return

        cifrado = pow(mensaje, e, n)
        descifrado = pow(cifrado, d, n)

        print(f"\nMensaje original: {mensaje}")
        print(f"Mensaje cifrado: {cifrado}")
        print(f"Mensaje descifrado: {descifrado}")

    except ValueError:
        print("Error: todos los valores deben ser números enteros.")


def exponenciacion_rapida():
    print("\n--- 3.3 EXPONENCIACIÓN RÁPIDA ---")

    try:
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        modulo = int(input("Ingrese el módulo: "))

        if exponente < 0:
            print("Error: el exponente debe ser mayor o igual a 0.")
            return

        if modulo <= 0:
            print("Error: el módulo debe ser mayor que 0.")
            return

        resultado = 1
        base_actual = base % modulo
        exponente_actual = exponente
        ronda = 1

        print("\nProcedimiento:")
        print("-" * 60)

        while exponente_actual > 0:
            print(
                f"Ronda {ronda}: "
                f"resultado={resultado}, "
                f"base={base_actual}, "
                f"exponente={exponente_actual}"
            )

            if exponente_actual % 2 == 1:
                resultado = (resultado * base_actual) % modulo

            base_actual = (base_actual * base_actual) % modulo
            exponente_actual //= 2
            ronda += 1

        print("-" * 60)
        print(
            f"\nResultado: {base}^{exponente} mod {modulo} = {resultado}"
        )

    except ValueError:
        print("Error: debe ingresar números enteros.")


# ============================================================
#                     4. HASH
# ============================================================

def hash_md5():
    print("\n--- 4.1 MD5 ---")

    texto = input("Ingrese el texto: ")

    resultado = hashlib.md5(
        texto.encode("utf-8")
    ).hexdigest()

    print(f"\nTexto: {texto}")
    print(f"MD5:   {resultado}")


def hash_sha256():
    print("\n--- 4.2 SHA-256 ---")

    texto = input("Ingrese el texto: ")

    resultado = hashlib.sha256(
        texto.encode("utf-8")
    ).hexdigest()

    print(f"\nTexto:   {texto}")
    print(f"SHA-256: {resultado}")


def hash_sha512():
    print("\n--- 4.3 SHA-512 ---")

    texto = input("Ingrese el texto: ")

    resultado = hashlib.sha512(
        texto.encode("utf-8")
    ).hexdigest()

    print(f"\nTexto:   {texto}")
    print(f"SHA-512: {resultado}")


# ============================================================
#                   5. CODIFICACIÓN
# ============================================================

def codificacion_ascii():
    print("\n--- 5.1 ASCII ---")

    opcion = input("¿Desea codificar o decodificar? (C/D): ").upper()

    if opcion == "C":
        texto = input("Ingrese el texto: ")

        resultado = []

        for caracter in texto:
            resultado.append(str(ord(caracter)))

        print(f"\nASCII: {' '.join(resultado)}")

    elif opcion == "D":
        valores = input(
            "Ingrese los valores ASCII separados por espacios: "
        )

        try:
            numeros = [int(x) for x in valores.split()]
            resultado = "".join(chr(x) for x in numeros)

            print(f"\nTexto: {resultado}")

        except ValueError:
            print("Error: valores ASCII inválidos.")

    else:
        print("Opción no válida.")


def codificacion_hexadecimal():
    print("\n--- 5.2 HEXADECIMAL ---")

    opcion = input("¿Desea codificar o decodificar? (C/D): ").upper()

    if opcion == "C":
        texto = input("Ingrese el texto: ")

        resultado = texto.encode("utf-8").hex()

        print(f"\nHexadecimal: {resultado}")

    elif opcion == "D":
        hexadecimal = input("Ingrese el hexadecimal: ")

        try:
            resultado = bytes.fromhex(hexadecimal).decode("utf-8")

            print(f"\nTexto: {resultado}")

        except ValueError:
            print("Error: hexadecimal inválido.")

    else:
        print("Opción no válida.")


def codificacion_binario():
    print("\n--- 5.3 BINARIO ---")

    opcion = input("¿Desea codificar o decodificar? (C/D): ").upper()

    if opcion == "C":
        texto = input("Ingrese el texto: ")

        resultado = " ".join(
            format(byte, "08b")
            for byte in texto.encode("utf-8")
        )

        print(f"\nBinario: {resultado}")

    elif opcion == "D":
        binario = input(
            "Ingrese los valores binarios separados por espacios: "
        )

        try:
            valores = binario.split()

            resultado = bytes(
                int(valor, 2) for valor in valores
            ).decode("utf-8")

            print(f"\nTexto: {resultado}")

        except ValueError:
            print("Error: binario inválido.")

    else:
        print("Opción no válida.")


def codificacion_base64():
    print("\n--- 5.4 BASE64 ---")

    opcion = input("¿Desea codificar o decodificar? (C/D): ").upper()

    if opcion == "C":
        texto = input("Ingrese el texto: ")

        resultado = base64.b64encode(
            texto.encode("utf-8")
        ).decode("utf-8")

        print(f"\nBase64: {resultado}")

    elif opcion == "D":
        texto = input("Ingrese el texto Base64: ")

        try:
            resultado = base64.b64decode(
                texto
            ).decode("utf-8")

            print(f"\nTexto: {resultado}")

        except Exception:
            print("Error: Base64 inválido.")

    else:
        print("Opción no válida.")


# ============================================================
#                        6. SALT
# ============================================================

def generar_salt():
    caracteres = string.ascii_letters + string.digits

    return "".join(
        secrets.choice(caracteres)
        for _ in range(16)
    )


def hash_con_salt(algoritmo):
    print(f"\n--- HASH {algoritmo.upper()} CON SALT ---")

    clave = input("Ingrese la clave: ")

    cantidad = int(
        input("¿Cuántos SALT diferentes desea generar?: ")
    )

    if cantidad <= 0:
        print("Error: la cantidad debe ser mayor que 0.")
        return

    print("\n" + "=" * 80)

    for i in range(1, cantidad + 1):
        salt = generar_salt()

        datos = (salt + clave).encode("utf-8")

        if algoritmo == "md5":
            hash_resultado = hashlib.md5(datos).hexdigest()

        elif algoritmo == "sha256":
            hash_resultado = hashlib.sha256(datos).hexdigest()

        elif algoritmo == "sha512":
            hash_resultado = hashlib.sha512(datos).hexdigest()

        print(f"\nSALT {i}: {salt}")
        print(f"HASH:   {hash_resultado}")

    print("\n" + "=" * 80)
    print("Cada SALT genera un hash diferente para la misma clave.")


# ============================================================
#                    MENÚ MATEMÁTICA
# ============================================================

def menu_matematica_modular():

    while True:

        print("\n" + "=" * 60)
        print("              MATEMÁTICA MODULAR")
        print("=" * 60)
        print("1.1 Calcular módulo")
        print("1.2 Inverso aditivo")
        print("1.3 Inverso de XOR")
        print("1.4 MCD e inverso multiplicativo")
        print("1.5 Inverso multiplicativo tradicional")
        print("1.6 Inverso multiplicativo con AEE")
        print("0. Regresar")
        print("=" * 60)

        opcion = input("Seleccione una opción: ")

        if opcion == "1.1":
            calcular_modulo()
            pausar()

        elif opcion == "1.2":
            inverso_aditivo()
            pausar()

        elif opcion == "1.3":
            inverso_xor()
            pausar()

        elif opcion == "1.4":
            calcular_mcd()
            pausar()

        elif opcion == "1.5":
            inverso_multiplicativo_tradicional()
            pausar()

        elif opcion == "1.6":
            inverso_multiplicativo_aee()
            pausar()

        elif opcion == "0":
            break

        else:
            print("\nOpción no válida.")


# ============================================================
#                  MENÚ CRIPTOGRAFÍA CLÁSICA
# ============================================================

def menu_criptografia_clasica():

    while True:

        print("\n" + "=" * 60)
        print("              CRIPTOGRAFÍA CLÁSICA")
        print("=" * 60)
        print("2.1 Cifrado Módulo 27")
        print("2.2 Cifrado César")
        print("2.3 Cifrado Vernam")
        print("2.4 Cifrado Atbash")
        print("2.5 Transposición columnar simple")
        print("2.6 Cifrado Afín")
        print("2.7 Cifra de Sustitución Simple")
        print("0. Regresar")
        print("=" * 60)

        opcion = input("Seleccione una opción: ")

        try:

            if opcion == "2.1":
                modulo_27()
                pausar()

            elif opcion == "2.2":
                cesar()
                pausar()

            elif opcion == "2.3":
                vernam()
                pausar()

            elif opcion == "2.4":
                atbash()
                pausar()

            elif opcion == "2.5":
                transposicion_columnar()
                pausar()

            elif opcion == "2.6":
                afin()
                pausar()

            elif opcion == "2.7":
                sustitucion_simple()
                pausar()

            elif opcion == "0":
                break

            else:
                print("\nOpción no válida.")

        except ValueError:
            print("\nError: ingresó un valor numérico incorrecto.")


# ============================================================
#                  MENÚ CRIPTOGRAFÍA MODERNA
# ============================================================

def menu_criptografia_moderna():

    while True:

        print("\n" + "=" * 60)
        print("              CRIPTOGRAFÍA MODERNA")
        print("=" * 60)
        print("3.1 Diffie-Hellman")
        print("3.2 RSA")
        print("3.3 Exponenciación rápida")
        print("0. Regresar")
        print("=" * 60)

        opcion = input("Seleccione una opción: ")

        try:

            if opcion == "3.1":
                diffie_hellman()
                pausar()

            elif opcion == "3.2":
                rsa()
                pausar()

            elif opcion == "3.3":
                exponenciacion_rapida()
                pausar()

            elif opcion == "0":
                break

            else:
                print("\nOpción no válida.")

        except ValueError:
            print("\nError: ingresó un valor numérico incorrecto.")


# ============================================================
#                         MENÚ HASH
# ============================================================

def menu_hash():

    while True:

        print("\n" + "=" * 60)
        print("                 ALGORITMOS HASH")
        print("=" * 60)
        print("4.1 MD5")
        print("4.2 SHA-256")
        print("4.3 SHA-512")
        print("0. Regresar")
        print("=" * 60)

        opcion = input("Seleccione una opción: ")

        if opcion == "4.1":
            hash_md5()
            pausar()

        elif opcion == "4.2":
            hash_sha256()
            pausar()

        elif opcion == "4.3":
            hash_sha512()
            pausar()

        elif opcion == "0":
            break

        else:
            print("\nOpción no válida.")


# ============================================================
#                     MENÚ CODIFICACIÓN
# ============================================================

def menu_codificacion():

    while True:

        print("\n" + "=" * 60)
        print("                    CODIFICACIÓN")
        print("=" * 60)
        print("5.1 ASCII")
        print("5.2 Hexadecimal")
        print("5.3 Binario")
        print("5.4 Base64")
        print("0. Regresar")
        print("=" * 60)

        opcion = input("Seleccione una opción: ")

        if opcion == "5.1":
            codificacion_ascii()
            pausar()

        elif opcion == "5.2":
            codificacion_hexadecimal()
            pausar()

        elif opcion == "5.3":
            codificacion_binario()
            pausar()

        elif opcion == "5.4":
            codificacion_base64()
            pausar()

        elif opcion == "0":
            break

        else:
            print("\nOpción no válida.")


# ============================================================
#                       MENÚ SALT
# ============================================================

def menu_salt():

    while True:

        print("\n" + "=" * 60)
        print("                    USO DE SALT")
        print("=" * 60)
        print("6.1 Hash MD5 con diferentes SALT")
        print("6.2 Hash SHA-256 con diferentes SALT")
        print("6.3 Hash SHA-512 con diferentes SALT")
        print("0. Regresar")
        print("=" * 60)

        opcion = input("Seleccione una opción: ")

        try:

            if opcion == "6.1":
                hash_con_salt("md5")
                pausar()

            elif opcion == "6.2":
                hash_con_salt("sha256")
                pausar()

            elif opcion == "6.3":
                hash_con_salt("sha512")
                pausar()

            elif opcion == "0":
                break

            else:
                print("\nOpción no válida.")

        except ValueError:
            print("\nError: ingrese un número válido.")


# ============================================================
#                    MENÚ PRINCIPAL
# ============================================================

def mostrar_menu_principal():

    while True:

        print("\n" + "=" * 65)
        print("                 CALCULADORA CRIPTOGRÁFICA")
        print("=" * 65)
        print("1. Operaciones matemáticas modulares")
        print("2. Criptografía clásica")
        print("3. Criptografía moderna")
        print("4. Algoritmos Hash")
        print("5. Codificación")
        print("6. Uso de SALT")
        print("0. Salir")
        print("=" * 65)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_matematica_modular()

        elif opcion == "2":
            menu_criptografia_clasica()

        elif opcion == "3":
            menu_criptografia_moderna()

        elif opcion == "4":
            menu_hash()

        elif opcion == "5":
            menu_codificacion()

        elif opcion == "6":
            menu_salt()

        elif opcion == "0":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción no válida.")


# ============================================================
#                       EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    mostrar_menu_principal()
