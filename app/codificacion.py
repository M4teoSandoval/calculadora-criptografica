"""5. CODIFICACION.

ASCII, hexadecimal, binario y Base64. Cada formato tiene su par de
funciones (codificar y decodificar) y un despachante que decide segun
la opcion C/D elegida en el menu.
"""

import base64
import binascii


def _validar_modo(modo: str) -> str:
    modo = modo.upper()

    if modo not in ("C", "D"):
        raise ValueError("Opción no válida.")

    return modo


def _respuesta(entrada: str, etiqueta: str, salida: str, modo: str) -> dict:
    return {
        "entrada": entrada,
        "etiqueta": etiqueta,
        "modo": "codificar" if modo == "C" else "decodificar",
        "salida": salida,
    }


# ----------------------------- 5.1 ASCII -----------------------------

def ascii_codificar(texto: str) -> dict:
    valores = [str(ord(caracter)) for caracter in texto]

    return _respuesta(texto, "ASCII", " ".join(valores), "C")


def ascii_decodificar(valores: str) -> dict:
    try:
        numeros = [int(valor) for valor in valores.split()]
        resultado = "".join(chr(numero) for numero in numeros)
    except ValueError:
        raise ValueError("Error: valores ASCII inválidos.")

    return _respuesta(valores, "Texto", resultado, "D")


def ascii_procesar(entrada: str, modo: str = "C") -> dict:
    if _validar_modo(modo) == "C":
        return ascii_codificar(entrada)

    return ascii_decodificar(entrada)


# ------------------------- 5.2 HEXADECIMAL --------------------------

def hexadecimal_codificar(texto: str) -> dict:
    return _respuesta(
        texto,
        "Hexadecimal",
        texto.encode("utf-8").hex(),
        "C",
    )


def hexadecimal_decodificar(hexadecimal: str) -> dict:
    try:
        resultado = bytes.fromhex(hexadecimal).decode("utf-8")
    except ValueError:
        raise ValueError("Error: hexadecimal inválido.")

    return _respuesta(hexadecimal, "Texto", resultado, "D")


def hexadecimal_procesar(entrada: str, modo: str = "C") -> dict:
    if _validar_modo(modo) == "C":
        return hexadecimal_codificar(entrada)

    return hexadecimal_decodificar(entrada)


# ---------------------------- 5.3 BINARIO ----------------------------

def binario_codificar(texto: str) -> dict:
    resultado = " ".join(
        format(byte, "08b") for byte in texto.encode("utf-8")
    )

    return _respuesta(texto, "Binario", resultado, "C")


def binario_decodificar(binario: str) -> dict:
    try:
        valores = binario.split()
        resultado = bytes(
            int(valor, 2) for valor in valores
        ).decode("utf-8")
    except ValueError:
        raise ValueError("Error: binario inválido.")

    return _respuesta(binario, "Texto", resultado, "D")


def binario_procesar(entrada: str, modo: str = "C") -> dict:
    if _validar_modo(modo) == "C":
        return binario_codificar(entrada)

    return binario_decodificar(entrada)


# ----------------------------- 5.4 BASE64 -----------------------------

def base64_codificar(texto: str) -> dict:
    resultado = base64.b64encode(texto.encode("utf-8")).decode("utf-8")

    return _respuesta(texto, "Base64", resultado, "C")


def base64_decodificar(texto: str) -> dict:
    try:
        resultado = base64.b64decode(texto).decode("utf-8")
    except (binascii.Error, ValueError):
        raise ValueError("Error: Base64 inválido.")

    return _respuesta(texto, "Texto", resultado, "D")


def base64_procesar(entrada: str, modo: str = "C") -> dict:
    if _validar_modo(modo) == "C":
        return base64_codificar(entrada)

    return base64_decodificar(entrada)
