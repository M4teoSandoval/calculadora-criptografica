"""6. USO DE SALT.

Generacion de sales aleatorias y hash de una misma clave con varias
sales distintas, para demostrar por que el SALT evita tablas precalculadas.
"""

import hashlib
import secrets
import string

from . import hashes


def generar_salt(longitud: int = 16) -> str:
    """Genera un SALT aleatorio de 16 caracteres alfanumericos."""
    caracteres = string.ascii_letters + string.digits

    return "".join(
        secrets.choice(caracteres) for _ in range(longitud)
    )


def hash_con_salt(clave: str, algoritmo: str, cantidad: int) -> dict:
    """Aplica el mismo hash 'cantidad' veces sobre la misma clave,
    usando un SALT diferente en cada intento."""
    if cantidad <= 0:
        raise ValueError("Error: la cantidad debe ser mayor que 0.")

    algoritmo = algoritmo.lower()

    if algoritmo not in hashes.HASHES:
        raise ValueError(
            f"Error: algoritmo de hash no soportado: {algoritmo}."
        )

    resultados = []

    for numero in range(1, cantidad + 1):
        salt = generar_salt()
        datos = (salt + clave).encode("utf-8")

        resultados.append({
            "numero": numero,
            "salt": salt,
            "hash": hashes.HASHES[algoritmo](datos).hexdigest(),
        })

    return {
        "clave": clave,
        "algoritmo": algoritmo,
        "cantidad": cantidad,
        "resultados": resultados,
    }
