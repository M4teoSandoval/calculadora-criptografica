"""Capa de dominio de la Calculadora Criptografica.

Este paquete concentra TODA la logica de los algoritmos del taller en
seis modulos, uno por cada seccion del menu. Ninguna funcion aqui pide
datos por consola ni imprime en pantalla: cada una recibe sus
parametros y devuelve un diccionario.

    matematica_modular   1. Módulo, inversos, MCD y AEE
    criptografia_clasica 2. César, Vernam, Atbash, afín, transposición...
    criptografia_moderna 3. Diffie-Hellman, RSA, exponenciación rápida
    hashes               4. MD5, SHA-256, SHA-512
    codificacion         5. ASCII, hexadecimal, binario, Base64
    salt                 6. Hash de claves con distintos SALT

Las dos interfaces del proyecto (la consola calculadora.py y la web
web/main.py) importan desde aqui, de modo que el algoritmo existe en
un solo lugar y la logica no se duplica.

Los errores de dominio se lanzan como ValueError con el texto que se
muestra al usuario.
"""

from . import (
    codificacion,
    criptografia_clasica,
    criptografia_moderna,
    hashes,
    matematica_modular,
    salt,
)

from .matematica_modular import (
    calcular_mcd,
    calcular_modulo,
    inverso_aditivo,
    inverso_multiplicativo_aee,
    inverso_multiplicativo_tradicional,
    inverso_xor,
)

from .criptografia_clasica import (
    afin,
    atbash,
    cesar,
    modulo_27,
    sustitucion_simple,
    transposicion_columnar,
    vernam,
)

from .criptografia_moderna import (
    diffie_hellman,
    exponenciacion_rapida,
    rsa,
    rsa_clave_privada,
    rsa_parametros,
)

from .hashes import hash_md5, hash_sha256, hash_sha512

from .codificacion import (
    ascii_codificar,
    ascii_decodificar,
    ascii_procesar,
    base64_codificar,
    base64_decodificar,
    base64_procesar,
    binario_codificar,
    binario_decodificar,
    binario_procesar,
    hexadecimal_codificar,
    hexadecimal_decodificar,
    hexadecimal_procesar,
)

from .salt import generar_salt, hash_con_salt


def mensaje_error(excepcion: BaseException) -> str:
    """Devuelve el texto de un error listo para mostrar.

    Los errores que escribe la capa app/ ya vienen con el prefijo
    'Error:'; los que provienen de la libreria estandar se completan.
    """
    texto = str(excepcion)

    if texto.startswith("Error:") or texto.startswith("Opción"):
        return texto

    return f"Error: {texto}"


__all__ = [
    "codificacion",
    "criptografia_clasica",
    "criptografia_moderna",
    "hashes",
    "matematica_modular",
    "salt",
    "calcular_modulo",
    "inverso_aditivo",
    "inverso_xor",
    "calcular_mcd",
    "inverso_multiplicativo_tradicional",
    "inverso_multiplicativo_aee",
    "modulo_27",
    "cesar",
    "vernam",
    "atbash",
    "transposicion_columnar",
    "afin",
    "sustitucion_simple",
    "diffie_hellman",
    "rsa",
    "rsa_parametros",
    "rsa_clave_privada",
    "exponenciacion_rapida",
    "hash_md5",
    "hash_sha256",
    "hash_sha512",
    "ascii_codificar",
    "ascii_decodificar",
    "ascii_procesar",
    "hexadecimal_codificar",
    "hexadecimal_decodificar",
    "hexadecimal_procesar",
    "binario_codificar",
    "binario_decodificar",
    "binario_procesar",
    "base64_codificar",
    "base64_decodificar",
    "base64_procesar",
    "generar_salt",
    "hash_con_salt",
    "mensaje_error",
]
