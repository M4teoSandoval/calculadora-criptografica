"""4. ALGORITMOS HASH.

MD5, SHA-256 y SHA-512 sobre texto plano en UTF-8.
"""

import hashlib

HASHES = {
    "md5": hashlib.md5,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


def _calcular(texto: str, algoritmo: str) -> dict:
    return {
        "texto": texto,
        "algoritmo": algoritmo,
        "hash": HASHES[algoritmo](texto.encode("utf-8")).hexdigest(),
    }


def hash_md5(texto: str) -> dict:
    """4.1 Calcula el hash MD5."""
    return _calcular(texto, "md5")


def hash_sha256(texto: str) -> dict:
    """4.2 Calcula el hash SHA-256."""
    return _calcular(texto, "sha256")


def hash_sha512(texto: str) -> dict:
    """4.3 Calcula el hash SHA-512."""
    return _calcular(texto, "sha512")
