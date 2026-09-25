"""1. MATEMATICA MODULAR.

Funciones puras: reciben datos y devuelven diccionarios de resultado.
No piden datos por consola ni escriben en pantalla; eso es tarea de
las interfaces (calculadora.py y web/main.py).
"""

import math


def calcular_modulo(a: int, n: int) -> dict:
    """1.1 Calcula a mod n."""
    if n == 0:
        raise ValueError("Error: el módulo n no puede ser 0.")

    return {
        "a": a,
        "n": n,
        "resultado": a % n,
    }


def inverso_aditivo(a: int, n: int) -> dict:
    """1.2 Calcula el inverso aditivo de a modulo n."""
    if n <= 0:
        raise ValueError("Error: el módulo debe ser mayor que 0.")

    inverso = (-a) % n

    return {
        "a": a,
        "n": n,
        "inverso": inverso,
        "comprobacion": (a + inverso) % n,
    }


def inverso_xor(a: int, b: int) -> dict:
    """1.3 Calcula a XOR b y demuestra que XOR es su propio inverso."""
    resultado = a ^ b

    return {
        "a": a,
        "b": b,
        "resultado": resultado,
        "recuperado": resultado ^ b,
    }


def calcular_mcd(a: int, n: int) -> dict:
    """1.4 Calcula MCD(a, n) e indica si existe inverso multiplicativo."""
    if n <= 0:
        raise ValueError("Error: el módulo debe ser mayor que 0.")

    mcd = math.gcd(a, n)
    existe = mcd == 1

    if not existe:
        return {
            "a": a,
            "n": n,
            "mcd": mcd,
            "existe_inverso": False,
            "inverso": None,
            "comprobacion": None,
        }

    inverso = pow(a, -1, n)

    return {
        "a": a,
        "n": n,
        "mcd": mcd,
        "existe_inverso": True,
        "inverso": inverso,
        "comprobacion": (a * inverso) % n,
    }


def inverso_multiplicativo_tradicional(a: int, n: int) -> dict:
    """1.5 Busca por fuerza bruta un x tal que (a * x) mod n = 1."""
    if n <= 0:
        raise ValueError("Error: el módulo debe ser mayor que 0.")

    mcd = math.gcd(a, n)

    if mcd != 1:
        return {
            "a": a,
            "n": n,
            "mcd": mcd,
            "existe_inverso": False,
            "inverso": None,
            "intentos": [],
        }

    intentos = []

    for x in range(1, n):
        valor = (a * x) % n
        intentos.append({"x": x, "valor": valor})

        if valor == 1:
            return {
                "a": a,
                "n": n,
                "mcd": mcd,
                "existe_inverso": True,
                "inverso": x,
                "intentos": intentos,
            }

    return {
        "a": a,
        "n": n,
        "mcd": mcd,
        "existe_inverso": False,
        "inverso": None,
        "intentos": intentos,
    }


def inverso_multiplicativo_aee(a: int, n: int) -> dict:
    """1.6 Inverso multiplicativo con el Algoritmo Extendido de Euclides.

    Devuelve ademas la tabla de rondas para que cada interfaz pueda
    mostrarla completa.
    """
    if n <= 0:
        raise ValueError("Error: el módulo debe ser mayor que 0.")

    a_original = a
    n_original = n

    if a < 0:
        a = a % n

    r0, r1 = n, a
    t0, t1 = 0, 1
    tabla = []

    while r1 != 0:
        cociente = r0 // r1
        residuo = r0 % r1

        tabla.append({
            "ronda": len(tabla) + 1,
            "r_anterior": r0,
            "r_actual": r1,
            "cociente": cociente,
            "residuo": residuo,
        })

        r0, r1 = r1, residuo
        t0, t1 = t1, t0 - cociente * t1

    mcd = r0

    if mcd != 1:
        return {
            "a": a_original,
            "n": n_original,
            "mcd": mcd,
            "existe_inverso": False,
            "inverso": None,
            "comprobacion": None,
            "rondas": len(tabla),
            "tabla": tabla,
        }

    inverso = t0 % n_original

    return {
        "a": a_original,
        "n": n_original,
        "mcd": mcd,
        "existe_inverso": True,
        "inverso": inverso,
        "comprobacion": (a_original * inverso) % n_original,
        "rondas": len(tabla),
        "tabla": tabla,
    }
