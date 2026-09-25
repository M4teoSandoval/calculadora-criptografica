"""3. CRIPTOGRAFIA MODERNA.

Diffie-Hellman, RSA y exponenciacion rapida. Al igual que el resto de
la capa app/, estas funciones no imprimen nada: describen el resultado
para que las dos interfaces lo muestren.
"""

import math


def diffie_hellman(p: int, g: int, a: int, b: int) -> dict:
    """3.1 Intercambio de claves Diffie-Hellman."""
    publica_alice = pow(g, a, p)
    publica_bob = pow(g, b, p)

    clave_alice = pow(publica_bob, a, p)
    clave_bob = pow(publica_alice, b, p)

    return {
        "p": p,
        "g": g,
        "a": a,
        "b": b,
        "publica_alice": publica_alice,
        "publica_bob": publica_bob,
        "clave_alice": clave_alice,
        "clave_bob": clave_bob,
        "coinciden": clave_alice == clave_bob,
    }


def rsa_parametros(p: int, q: int) -> dict:
    """3.2 Calcule n = p * q y el indicador de Euler \u03c6(n)."""
    n = p * q

    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": (p - 1) * (q - 1),
    }


def rsa_clave_privada(p: int, q: int, e: int) -> dict:
    """3.2 Calcula la clave privada d a partir del exponente e."""
    parametros = rsa_parametros(p, q)
    phi = parametros["phi"]

    if math.gcd(e, phi) != 1:
        raise ValueError("Error: e debe ser coprimo con \u03c6(n).")

    d = pow(e, -1, phi)
    n = parametros["n"]

    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "e": e,
        "d": d,
        "clave_publica": f"(e={e}, n={n})",
        "clave_privada": f"(d={d}, n={n})",
    }


def rsa(p: int, q: int, e: int, mensaje: int) -> dict:
    """3.2 Cifrado RSA de un mensaje numerico."""
    claves = rsa_clave_privada(p, q, e)

    if mensaje < 0 or mensaje >= claves["n"]:
        raise ValueError("Error: el mensaje debe estar entre 0 y n-1.")

    n = claves["n"]
    d = claves["d"]

    cifrado = pow(mensaje, claves["e"], n)
    descifrado = pow(cifrado, d, n)

    return {
        **claves,
        "mensaje": mensaje,
        "cifrado": cifrado,
        "descifrado": descifrado,
    }


def exponenciacion_rapida(base: int, exponente: int, modulo: int) -> dict:
    """3.3 Exponenciacion rapida por cuadrado binario, con sus rondas."""
    if exponente < 0:
        raise ValueError(
            "Error: el exponente debe ser mayor o igual a 0."
        )

    if modulo <= 0:
        raise ValueError("Error: el módulo debe ser mayor que 0.")

    resultado = 1
    base_actual = base % modulo
    exponente_actual = exponente
    rondas = []

    while exponente_actual > 0:
        rondas.append({
            "ronda": len(rondas) + 1,
            "resultado": resultado,
            "base": base_actual,
            "exponente": exponente_actual,
        })

        if exponente_actual % 2 == 1:
            resultado = (resultado * base_actual) % modulo

        base_actual = (base_actual * base_actual) % modulo
        exponente_actual //= 2

    return {
        "base": base,
        "exponente": exponente,
        "modulo": modulo,
        "rondas": rondas,
        "resultado": resultado,
    }
