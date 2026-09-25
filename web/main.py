"""Interfaz web de la Calculadora Criptografica.

Este archivo NO contiene algoritmos: solo declara las 24 herramientas
del taller y las conecta con las funciones puras del paquete app/.
La consola (calculadora.py) usa esas mismas funciones, de modo que la
logica criptografica vive en un unico lugar.
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import (
    codificacion,
    criptografia_clasica,
    criptografia_moderna,
    hashes,
    matematica_modular,
    mensaje_error,
    salt,
)

BASE = Path(__file__).resolve().parent

app = FastAPI(
    title="Calculadora Criptográfica",
    description="Calculadora de operaciones y algoritmos criptográficos",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE / "static")),
    name="static",
)

plantillas = Jinja2Templates(directory=str(BASE / "templates"))


# ============================================================
# AYUDAS PARA DECLARAR LOS FORMULARIOS
# ============================================================

def numero(nombre, etiqueta, extra=""):
    return {
        "name": nombre,
        "label": etiqueta,
        "type": "number",
        "extra": extra,
    }


def texto(nombre, etiqueta, extra=""):
    return {
        "name": nombre,
        "label": etiqueta,
        "type": "text",
        "extra": extra,
    }


def elegir(nombre, etiqueta, opciones):
    return {
        "name": nombre,
        "label": etiqueta,
        "type": "select",
        "options": opciones,
    }


CIFRAR = [("C", "Cifrar"), ("D", "Descifrar")]
CONVERTIR = [("C", "Codificar"), ("D", "Decodificar")]


# ============================================================
# SECCIONES DEL MENÚ
# ============================================================

SECCIONES = [
    {
        "clave": "modular",
        "numero": "1",
        "titulo": "Operaciones matemáticas modulares",
        "descripcion": "Módulo, inversos, MCD y Algoritmo Extendido "
                       "de Euclides con su tabla de rondas.",
        "resumen": "6 algoritmos",
    },
    {
        "clave": "clasica",
        "numero": "2",
        "titulo": "Criptografía clásica",
        "descripcion": "César, Vernam, Atbash, afín, módulo 27, "
                       "transposición y sustitución simple.",
        "resumen": "7 algoritmos",
    },
    {
        "clave": "moderna",
        "numero": "3",
        "titulo": "Criptografía moderna",
        "descripcion": "Diffie-Hellman, RSA y exponenciación rápida "
                       "por cuadrado binario.",
        "resumen": "3 algoritmos",
    },
    {
        "clave": "hash",
        "numero": "4",
        "titulo": "Algoritmos Hash",
        "descripcion": "MD5, SHA-256 y SHA-512 sobre texto en UTF-8.",
        "resumen": "3 algoritmos",
    },
    {
        "clave": "codificacion",
        "numero": "5",
        "titulo": "Codificación",
        "descripcion": "ASCII, hexadecimal, binario y Base64, "
                       "codificando y decodificando.",
        "resumen": "4 formatos",
    },
    {
        "clave": "salt",
        "numero": "6",
        "titulo": "Uso de SALT",
        "descripcion": "El mismo hash de una misma clave con sales "
                       "aleatorias diferentes.",
        "resumen": "3 algoritmos",
    },
]


# ============================================================
# HERRAMIENTAS
#
# Cada entrada describe un formulario y la funcion de app/ que
# ejecuta. Agregar un algoritmo al taller es agregar una entrada
# aqui: no hay que escribir ni una ruta ni una plantilla nueva.
# ============================================================

HERRAMIENTAS = [
    # ------------------------- 1. MODULAR -------------------------
    {
        "seccion": "modular",
        "codigo": "1.1",
        "slug": "modulo",
        "titulo": "Calcular módulo",
        "descripcion": "Calcula el resultado de a mod n.",
        "funcion": matematica_modular.calcular_modulo,
        "campos": [
            numero("a", "Número a"),
            numero("n", "Módulo n"),
        ],
    },
    {
        "seccion": "modular",
        "codigo": "1.2",
        "slug": "inverso-aditivo",
        "titulo": "Calcular inverso aditivo",
        "descripcion": "Elemento que suma cero módulo n.",
        "funcion": matematica_modular.inverso_aditivo,
        "campos": [
            numero("a", "Número a"),
            numero("n", "Módulo n", "min='1'"),
        ],
    },
    {
        "seccion": "modular",
        "codigo": "1.3",
        "slug": "inverso-xor",
        "titulo": "Calcular inverso de XOR",
        "descripcion": "XOR es su propio inverso: se comprueba al "
                       "repetir la operación.",
        "funcion": matematica_modular.inverso_xor,
        "campos": [
            numero("a", "Primer número"),
            numero("b", "Segundo número"),
        ],
    },
    {
        "seccion": "modular",
        "codigo": "1.4",
        "slug": "mcd",
        "titulo": "Máximo común divisor",
        "descripcion": "Calcula MCD(a, n) e indica si existe el "
                       "inverso multiplicativo.",
        "funcion": matematica_modular.calcular_mcd,
        "campos": [
            numero("a", "Número a"),
            numero("n", "Módulo n", "min='1'"),
        ],
    },
    {
        "seccion": "modular",
        "codigo": "1.5",
        "slug": "inverso-tradicional",
        "titulo": "Inverso multiplicativo tradicional",
        "descripcion": "Busca por método tradicional un x tal que "
                       "(a × x) mod n = 1.",
        "funcion": (
            matematica_modular.inverso_multiplicativo_tradicional
        ),
        "campos": [
            numero("a", "Número a"),
            numero("n", "Módulo n", "min='1'"),
        ],
    },
    {
        "seccion": "modular",
        "codigo": "1.6",
        "slug": "aee",
        "titulo": "Algoritmo Extendido de Euclides",
        "descripcion": "Inverso multiplicativo por AEE, indicando "
                       "cuántas rondas y mostrando la tabla completa.",
        "funcion": matematica_modular.inverso_multiplicativo_aee,
        "campos": [
            numero("a", "Número a"),
            numero("n", "Módulo n", "min='1'"),
        ],
    },

    # ------------------------- 2. CLÁSICA -------------------------
    {
        "seccion": "clasica",
        "codigo": "2.1",
        "slug": "modulo-27",
        "titulo": "Cifrado Módulo 27",
        "descripcion": "Cifra sobre un alfabeto de 27 símbolos "
                       "(espacio más A-Z).",
        "funcion": criptografia_clasica.modulo_27,
        "campos": [
            texto("texto", "Texto"),
            numero("desplazamiento", "Desplazamiento"),
        ],
    },
    {
        "seccion": "clasica",
        "codigo": "2.2",
        "slug": "cesar",
        "titulo": "Cifrado César",
        "descripcion": "Desplaza cada letra un número fijo de "
                       "posiciones.",
        "funcion": criptografia_clasica.cesar,
        "campos": [
            texto("texto", "Texto"),
            numero("desplazamiento", "Desplazamiento"),
            elegir("modo", "Operación", CIFRAR),
        ],
        "ensamblar": lambda v: {
            "texto": v["texto"],
            "desplazamiento": v["desplazamiento"],
            "descifrar": v["modo"] == "D",
        },
    },
    {
        "seccion": "clasica",
        "codigo": "2.3",
        "slug": "vernam",
        "titulo": "Cifrado Vernam",
        "descripcion": "Aplica XOR entre texto y clave, que deben "
                       "tener la misma longitud.",
        "funcion": criptografia_clasica.vernam,
        "campos": [
            texto("texto", "Texto"),
            texto("clave", "Clave"),
        ],
    },
    {
        "seccion": "clasica",
        "codigo": "2.4",
        "slug": "atbash",
        "titulo": "Cifrado Atbash",
        "descripcion": "Refleja el alfabeto: A↔Z, B↔Y, C↔X.",
        "funcion": criptografia_clasica.atbash,
        "campos": [
            texto("texto", "Texto"),
        ],
    },
    {
        "seccion": "clasica",
        "codigo": "2.5",
        "slug": "transposicion-columnar",
        "titulo": "Transposición columnar simple",
        "descripcion": "Escribe el texto en una matriz y lee las "
                       "columnas.",
        "funcion": criptografia_clasica.transposicion_columnar,
        "campos": [
            texto("texto", "Texto (los espacios se ignoran)"),
            numero("columnas", "Número de columnas", "min='1'"),
        ],
    },
    {
        "seccion": "clasica",
        "codigo": "2.6",
        "slug": "afin",
        "titulo": "Cifrado afín",
        "descripcion": "y = (a · x + b) mod 26, con a coprimo "
                       "con 26.",
        "funcion": criptografia_clasica.afin,
        "campos": [
            texto("texto", "Texto"),
            numero("a", "Valor de a"),
            numero("b", "Valor de b"),
            elegir("modo", "Operación", CIFRAR),
        ],
    },
    {
        "seccion": "clasica",
        "codigo": "2.7",
        "slug": "sustitucion-simple",
        "titulo": "Sustitución simple",
        "descripcion": "Sustituye cada letra con el alfabeto de 26 "
                       "letras que se indique.",
        "funcion": criptografia_clasica.sustitucion_simple,
        "campos": [
            texto("clave", "Alfabeto de sustitución (26 letras)",
                  "maxlength='26'"),
            texto("texto", "Texto"),
            elegir("modo", "Operación", CIFRAR),
        ],
    },

    # ------------------------- 3. MODERNA -------------------------
    {
        "seccion": "moderna",
        "codigo": "3.1",
        "slug": "diffie-hellman",
        "titulo": "Diffie-Hellman",
        "descripcion": "Intercambio de claves sobre un primo p y una "
                       "raíz primitiva g.",
        "funcion": criptografia_moderna.diffie_hellman,
        "campos": [
            numero("p", "Número primo p"),
            numero("g", "Raíz primitiva g"),
            numero("a", "Clave privada de Alice"),
            numero("b", "Clave privada de Bob"),
        ],
    },
    {
        "seccion": "moderna",
        "codigo": "3.2",
        "slug": "rsa",
        "titulo": "RSA",
        "descripcion": "Calcula n, φ(n), las claves y cifra un mensaje "
                       "numérico.",
        "funcion": criptografia_moderna.rsa,
        "campos": [
            numero("p", "Número primo p"),
            numero("q", "Número primo q"),
            numero("e", "Exponente e"),
            numero("mensaje", "Mensaje (menor que n)", "min='0'"),
        ],
    },
    {
        "seccion": "moderna",
        "codigo": "3.3",
        "slug": "exponenciacion-rapida",
        "titulo": "Exponenciación rápida",
        "descripcion": "base^exponente mod módulo por cuadrado "
                       "binario, ronda a ronda.",
        "funcion": criptografia_moderna.exponenciacion_rapida,
        "campos": [
            numero("base", "Base"),
            numero("exponente", "Exponente", "min='0'"),
            numero("modulo", "Módulo", "min='1'"),
        ],
    },

    # -------------------------- 4. HASH ---------------------------
    {
        "seccion": "hash",
        "codigo": "4.1",
        "slug": "md5",
        "titulo": "MD5",
        "descripcion": "Huella de 128 bits del texto.",
        "funcion": hashes.hash_md5,
        "campos": [
            texto("texto", "Texto"),
        ],
    },
    {
        "seccion": "hash",
        "codigo": "4.2",
        "slug": "sha256",
        "titulo": "SHA-256",
        "descripcion": "Huella de 256 bits del texto.",
        "funcion": hashes.hash_sha256,
        "campos": [
            texto("texto", "Texto"),
        ],
    },
    {
        "seccion": "hash",
        "codigo": "4.3",
        "slug": "sha512",
        "titulo": "SHA-512",
        "descripcion": "Huella de 512 bits del texto.",
        "funcion": hashes.hash_sha512,
        "campos": [
            texto("texto", "Texto"),
        ],
    },

    # ---------------------- 5. CODIFICACIÓN ----------------------
    {
        "seccion": "codificacion",
        "codigo": "5.1",
        "slug": "ascii",
        "titulo": "ASCII",
        "descripcion": "Convierte cada carácter en su código decimal.",
        "funcion": codificacion.ascii_procesar,
        "campos": [
            elegir("modo", "Operación", CONVERTIR),
            texto("entrada", "Texto, o valores separados por espacios"),
        ],
    },
    {
        "seccion": "codificacion",
        "codigo": "5.2",
        "slug": "hexadecimal",
        "titulo": "Hexadecimal",
        "descripcion": "Convierte el texto UTF-8 a hexadecimal.",
        "funcion": codificacion.hexadecimal_procesar,
        "campos": [
            elegir("modo", "Operación", CONVERTIR),
            texto("entrada", "Texto, o cadena hexadecimal"),
        ],
    },
    {
        "seccion": "codificacion",
        "codigo": "5.3",
        "slug": "binario",
        "titulo": "Binario",
        "descripcion": "Convierte cada byte a 8 bits.",
        "funcion": codificacion.binario_procesar,
        "campos": [
            elegir("modo", "Operación", CONVERTIR),
            texto("entrada", "Texto, o bytes separados por espacios"),
        ],
    },
    {
        "seccion": "codificacion",
        "codigo": "5.4",
        "slug": "base64",
        "titulo": "Base64",
        "descripcion": "Codificación Base64 en base 64.",
        "funcion": codificacion.base64_procesar,
        "campos": [
            elegir("modo", "Operación", CONVERTIR),
            texto("entrada", "Texto, o texto en Base64"),
        ],
    },

    # -------------------------- 6. SALT ---------------------------
    {
        "seccion": "salt",
        "codigo": "6.1",
        "slug": "md5",
        "titulo": "Hash MD5 con SALT",
        "descripcion": "La misma clave con varios SALT distintos.",
        "funcion": salt.hash_con_salt,
        "campos": [
            texto("clave", "Clave"),
            numero("cantidad", "Cuántos SALT generar", "min='1'"),
        ],
        "ensamblar": lambda v: {
            "clave": v["clave"],
            "algoritmo": "md5",
            "cantidad": v["cantidad"],
        },
    },
    {
        "seccion": "salt",
        "codigo": "6.2",
        "slug": "sha256",
        "titulo": "Hash SHA-256 con SALT",
        "descripcion": "La misma clave con varios SALT distintos.",
        "funcion": salt.hash_con_salt,
        "campos": [
            texto("clave", "Clave"),
            numero("cantidad", "Cuántos SALT generar", "min='1'"),
        ],
        "ensamblar": lambda v: {
            "clave": v["clave"],
            "algoritmo": "sha256",
            "cantidad": v["cantidad"],
        },
    },
    {
        "seccion": "salt",
        "codigo": "6.3",
        "slug": "sha512",
        "titulo": "Hash SHA-512 con SALT",
        "descripcion": "La misma clave con varios SALT distintos.",
        "funcion": salt.hash_con_salt,
        "campos": [
            texto("clave", "Clave"),
            numero("cantidad", "Cuántos SALT generar", "min='1'"),
        ],
        "ensamblar": lambda v: {
            "clave": v["clave"],
            "algoritmo": "sha512",
            "cantidad": v["cantidad"],
        },
    },
]


# ============================================================
# FÓRMULA DE CADA HERRAMIENTA
# ============================================================

FORMULAS = {
    "1.1": "a mod n = b",
    "1.2": "(a + a-inverso) mod n = 0",
    "1.3": "a XOR b = c  ·  c XOR b = a",
    "1.4": "MCD(a, n) = 1  =>  existe a-inverso",
    "1.5": "a · x ≡ 1 (mod n)",
    "1.6": "r(i-1) = q(i) · r(i) + r(i+1)",
    "2.1": "c = (p + k) mod 27",
    "2.2": "c = (p + k) mod 26",
    "2.3": "c(i) = p(i) XOR k(i)",
    "2.4": "c = 25 - p",
    "2.5": "c = lectura por columnas de la matriz",
    "2.6": "c = (a · p + b) mod 26",
    "2.7": "c = clave[posicion de la letra]",
    "3.1": "A = g^a mod p  ·  B = g^b mod p  ·  k = B^a = A^b",
    "3.2": "c = m^e mod n  ·  m = c^d mod n",
    "3.3": "base^exponente mod modulo  (cuadrado binario)",
    "4.1": "MD5(texto) = 128 bits",
    "4.2": "SHA-256(texto) = 256 bits",
    "4.3": "SHA-512(texto) = 512 bits",
    "5.1": "codigo = ord(caracter)",
    "5.2": "texto -> bytes UTF-8 -> hexadecimal",
    "5.3": "byte = 8 bits",
    "5.4": "3 bytes -> 4 caracteres Base64",
    "6.1": "hash = HASH(SALT + clave)",
    "6.2": "hash = HASH(SALT + clave)",
    "6.3": "hash = HASH(SALT + clave)",
}

for herramienta in HERRAMIENTAS:
    herramienta["formula"] = FORMULAS[herramienta["codigo"]]


# ============================================================
# BÚSQUEDAS SOBRE EL REGISTRO
# ============================================================

def buscar_seccion(clave: str) -> dict:
    for seccion in SECCIONES:
        if seccion["clave"] == clave:
            return seccion

    raise HTTPException(status_code=404, detail="Sección no encontrada.")


def buscar_herramienta(clave_seccion: str, slug: str) -> dict:
    for herramienta in HERRAMIENTAS:
        if (
            herramienta["seccion"] == clave_seccion
            and herramienta["slug"] == slug
        ):
            return herramienta

    raise HTTPException(
        status_code=404,
        detail="Herramienta no encontrada.",
    )


def leer_valores(herramienta: dict, form) -> dict:
    """Convierte el formulario recibido en los argumentos de app/."""
    valores = {}

    for campo in herramienta["campos"]:
        crudo = str(form.get(campo["name"], "")).strip()

        if campo["type"] == "number":
            try:
                valores[campo["name"]] = int(crudo)
            except ValueError:
                raise ValueError(
                    f"Error: «{campo['label']}» debe ser un número "
                    f"entero."
                )
        else:
            valores[campo["name"]] = crudo

    ensamblar = herramienta.get("ensamblar")

    if ensamblar is not None:
        return ensamblar(valores)

    return valores


# ============================================================
# FILTRO DE LAS PLANTILLAS
# ============================================================

def prettificar(clave: str) -> str:
    """Convierte una clave de diccionario en etiqueta legible."""
    texto = clave.replace("_", " ").strip()

    if not texto:
        return clave

    return texto[0].upper() + texto[1:]


plantillas.env.filters["prettificar"] = prettificar


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "application": "Calculadora Criptográfica",
        "herramientas": len(HERRAMIENTAS),
    }


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):

    return plantillas.TemplateResponse(
        request,
        "index.html",
        {
            "request": request,
            "secciones": SECCIONES,
            "total": len(HERRAMIENTAS),
        },
    )


# ============================================================
# MENÚ DE CADA SECCIÓN
# ============================================================

@app.get("/{seccion}", response_class=HTMLResponse)
def menu(request: Request, seccion: str):

    datos = buscar_seccion(seccion)

    herramientas = [
        herramienta
        for herramienta in HERRAMIENTAS
        if herramienta["seccion"] == seccion
    ]

    return plantillas.TemplateResponse(
        request,
        "menu.html",
        {
            "request": request,
            "seccion": datos,
            "herramientas": herramientas,
        },
    )


# ============================================================
# FORMULARIO DE CADA HERRAMIENTA
# ============================================================

@app.get("/{seccion}/{slug}", response_class=HTMLResponse)
def formulario(request: Request, seccion: str, slug: str):

    datos = buscar_seccion(seccion)
    herramienta = buscar_herramienta(seccion, slug)

    return plantillas.TemplateResponse(
        request,
        "formulario.html",
        {
            "request": request,
            "seccion": datos,
            "herramienta": herramienta,
        },
    )


# ============================================================
# EJECUCIÓN DE CADA HERRAMIENTA
# ============================================================

@app.post("/{seccion}/{slug}", response_class=HTMLResponse)
async def ejecutar(request: Request, seccion: str, slug: str):

    datos = buscar_seccion(seccion)
    herramienta = buscar_herramienta(seccion, slug)

    contexto = {
        "request": request,
        "seccion": datos,
        "herramienta": herramienta,
    }

    try:
        argumentos = leer_valores(herramienta, await request.form())
        resultado = herramienta["funcion"](**argumentos)
    except ValueError as error:
        return plantillas.TemplateResponse(
            request,
            "resultado.html",
            {
                **contexto,
                "error": mensaje_error(error),
                "resultado": None,
            },
        )

    return plantillas.TemplateResponse(
        request,
        "resultado.html",
        {
            **contexto,
            "error": None,
            "resultado": resultado,
        },
    )
