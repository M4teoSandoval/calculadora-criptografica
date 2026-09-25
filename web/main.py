from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

import calculadora


app = FastAPI(
    title="Calculadora Criptográfica",
    description="Calculadora de operaciones y algoritmos criptográficos",
    version="1.0.0"
)


# ============================================================
# ESTILOS GENERALES
# ============================================================

STYLE = """
<style>
    * {
        box-sizing: border-box;
    }

    body {
        font-family: Arial, sans-serif;
        background: #0f172a;
        color: white;
        margin: 0;
        padding: 30px 20px;
    }

    .container {
        max-width: 900px;
        margin: auto;
    }

    .small-container {
        max-width: 650px;
        margin: auto;
    }

    a {
        color: #60a5fa;
        text-decoration: none;
    }

    h1 {
        margin-top: 25px;
        margin-bottom: 10px;
    }

    h2 {
        margin-bottom: 10px;
    }

    .description {
        color: #94a3b8;
        line-height: 1.5;
    }

    .options {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(250px, 1fr));
        gap: 15px;
        margin-top: 30px;
    }

    .option {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
    }

    .option h3 {
        margin-bottom: 8px;
    }

    .option p {
        color: #94a3b8;
        margin-bottom: 15px;
        line-height: 1.4;
    }

    .btn {
        display: block;
        width: 100%;
        padding: 12px;
        border-radius: 7px;
        border: none;
        background: #3b82f6;
        color: white;
        text-decoration: none;
        text-align: center;
        cursor: pointer;
        font-size: 15px;
    }

    .btn:hover {
        background: #2563eb;
    }

    form {
        background: #1e293b;
        padding: 25px;
        border-radius: 12px;
        margin-top: 25px;
        border: 1px solid #334155;
    }

    label {
        display: block;
        margin-bottom: 7px;
        margin-top: 15px;
        font-weight: bold;
    }

    input {
        width: 100%;
        padding: 12px;
        border-radius: 7px;
        border: 1px solid #475569;
        background: #0f172a;
        color: white;
        font-size: 16px;
    }

    button {
        width: 100%;
        margin-top: 20px;
        padding: 12px;
        border: none;
        border-radius: 7px;
        background: #3b82f6;
        color: white;
        font-size: 16px;
        cursor: pointer;
    }

    button:hover {
        background: #2563eb;
    }

    .result {
        margin-top: 20px;
        background: #172554;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #2563eb;
    }

    .error {
        margin-top: 20px;
        background: #450a0a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #991b1b;
    }

    .success {
        color: #86efac;
    }

    .danger {
        color: #fca5a5;
    }

    .formula {
        background: #0f172a;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
        font-family: monospace;
        overflow-x: auto;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        font-size: 14px;
    }

    th, td {
        border: 1px solid #475569;
        padding: 10px;
        text-align: center;
    }

    th {
        background: #334155;
    }

    td {
        background: #1e293b;
    }

    .table-container {
        overflow-x: auto;
    }

    .actions {
        display: grid;
        gap: 10px;
        margin-top: 20px;
    }

    @media (max-width: 600px) {
        body {
            padding: 20px 12px;
        }

        table {
            font-size: 12px;
        }
    }
</style>
"""


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

@app.get("/", response_class=HTMLResponse)
def inicio():

    return f"""
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <title>Calculadora Criptográfica</title>

        {STYLE}
    </head>

    <body>

        <div class="container">

            <h1>🔐 Calculadora Criptográfica</h1>

            <p class="description">
                Herramienta académica de Ciberseguridad
            </p>

            <div class="options">

                <div class="option">
                    <h2>1. Matemática Modular</h2>

                    <p>
                        Módulo, inversos, MCD y
                        Algoritmo Extendido de Euclides.
                    </p>

                    <a class="btn" href="/modular">
                        Ingresar
                    </a>
                </div>

                <div class="option">
                    <h2>2. Criptografía Clásica</h2>
                    <p>
                        César, Vernam, Atbash, Afín,
                        Módulo 27 y sustitución.
                    </p>
                    <button disabled>
                        Próximamente
                    </button>
                </div>

                <div class="option">
                    <h2>3. Criptografía Moderna</h2>
                    <p>
                        Diffie-Hellman, RSA y
                        exponenciación rápida.
                    </p>
                    <button disabled>
                        Próximamente
                    </button>
                </div>

                <div class="option">
                    <h2>4. Algoritmos Hash</h2>
                    <p>
                        MD5, SHA-256 y SHA-512.
                    </p>
                    <button disabled>
                        Próximamente
                    </button>
                </div>

                <div class="option">
                    <h2>5. Codificación</h2>
                    <p>
                        ASCII, hexadecimal,
                        binario y Base64.
                    </p>
                    <button disabled>
                        Próximamente
                    </button>
                </div>

                <div class="option">
                    <h2>6. Uso de SALT</h2>
                    <p>
                        Hash de contraseñas utilizando
                        diferentes valores de SALT.
                    </p>
                    <button disabled>
                        Próximamente
                    </button>
                </div>

            </div>

        </div>

    </body>
    </html>
    """


# ============================================================
# MENÚ MATEMÁTICA MODULAR
# ============================================================

@app.get("/modular", response_class=HTMLResponse)
def menu_modular():

    return f"""
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <title>Matemática Modular</title>
        {STYLE}
    </head>

    <body>

        <div class="container">

            <a href="/">
                ← Volver al inicio
            </a>

            <h1>1. Matemática Modular</h1>

            <p class="description">
                Selecciona la operación que deseas realizar.
            </p>

            <div class="options">

                <div class="option">
                    <h3>1.1 Módulo</h3>
                    <p>Calcula a mod n.</p>
                    <a class="btn" href="/modular/modulo">
                        Abrir
                    </a>
                </div>

                <div class="option">
                    <h3>1.2 Inverso aditivo</h3>
                    <p>
                        Calcula el inverso aditivo
                        de un número módulo n.
                    </p>
                    <a class="btn"
                       href="/modular/inverso-aditivo">
                        Abrir
                    </a>
                </div>

                <div class="option">
                    <h3>1.3 Inverso XOR</h3>
                    <p>
                        Realiza XOR y comprueba
                        su reversibilidad.
                    </p>
                    <a class="btn"
                       href="/modular/inverso-xor">
                        Abrir
                    </a>
                </div>

                <div class="option">
                    <h3>1.4 MCD</h3>
                    <p>
                        Calcula el MCD e indica
                        si existe inverso multiplicativo.
                    </p>
                    <a class="btn"
                       href="/modular/mcd">
                        Abrir
                    </a>
                </div>

                <div class="option">
                    <h3>1.5 Inverso tradicional</h3>
                    <p>
                        Encuentra el inverso multiplicativo
                        mediante búsqueda tradicional.
                    </p>
                    <a class="btn"
                       href="/modular/inverso-tradicional">
                        Abrir
                    </a>
                </div>

                <div class="option">
                    <h3>1.6 AEE</h3>
                    <p>
                        Algoritmo Extendido de Euclides
                        mostrando las rondas y la tabla.
                    </p>
                    <a class="btn"
                       href="/modular/aee">
                        Abrir
                    </a>
                </div>

            </div>

        </div>

    </body>
    </html>
    """


# ============================================================
# FUNCIÓN PARA CREAR PÁGINAS DE FORMULARIO
# ============================================================

def formulario_base(
    titulo,
    descripcion,
    campos,
    action
):

    campos_html = ""

    for campo in campos:
        campos_html += f"""
        <label for="{campo['name']}">
            {campo['label']}
        </label>

        <input
            type="{campo.get('type', 'number')}"
            id="{campo['name']}"
            name="{campo['name']}"
            {campo.get('extra', '')}
            required
        >
        """

    return f"""
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <title>{titulo}</title>
        {STYLE}
    </head>

    <body>

        <div class="small-container">

            <a href="/modular">
                ← Volver a Matemática Modular
            </a>

            <h1>{titulo}</h1>

            <p class="description">
                {descripcion}
            </p>

            <form method="post" action="{action}">

                {campos_html}

                <button type="submit">
                    CALCULAR
                </button>

            </form>

        </div>

    </body>

    </html>
    """


# ============================================================
# 1.1 MÓDULO
# ============================================================

@app.get("/modular/modulo", response_class=HTMLResponse)
def pagina_modulo():

    return formulario_base(
        "1.1 Calcular módulo",
        "Calcula el resultado de a mod n.",
        [
            {
                "name": "a",
                "label": "Número a"
            },
            {
                "name": "n",
                "label": "Módulo n",
                "extra": "min='1'"
            }
        ],
        "/modular/modulo"
    )


@app.post("/modular/modulo", response_class=HTMLResponse)
def calcular_modulo(
    a: int = Form(...),
    n: int = Form(...)
):

    if n <= 0:

        resultado = """
        <div class="error">
            El módulo n debe ser mayor que 0.
        </div>
        """

    else:

        resultado_calculo = a % n

        resultado = f"""
        <div class="result">

            <h2>Resultado</h2>

            <div class="formula">
                {a} mod {n} = {resultado_calculo}
            </div>

        </div>
        """

    return pagina_resultado(
        "1.1 Módulo",
        resultado
    )


# ============================================================
# 1.2 INVERSO ADITIVO
# ============================================================

@app.get("/modular/inverso-aditivo",
         response_class=HTMLResponse)
def pagina_inverso_aditivo():

    return formulario_base(
        "1.2 Inverso aditivo",
        "Calcula el inverso aditivo de a módulo n.",
        [
            {
                "name": "a",
                "label": "Número a"
            },
            {
                "name": "n",
                "label": "Módulo n",
                "extra": "min='1'"
            }
        ],
        "/modular/inverso-aditivo"
    )


@app.post("/modular/inverso-aditivo",
          response_class=HTMLResponse)
def calcular_inverso_aditivo(
    a: int = Form(...),
    n: int = Form(...)
):

    if n <= 0:

        resultado = """
        <div class="error">
            El módulo n debe ser mayor que 0.
        </div>
        """

    else:

        inverso = (-a) % n

        resultado = f"""
        <div class="result">

            <h2>Resultado</h2>

            <div class="formula">
                Inverso aditivo de {a} mod {n}
                = {inverso}
            </div>

            <p>
                Comprobación:
                ({a} + {inverso}) mod {n}
                = {(a + inverso) % n}
            </p>

        </div>
        """

    return pagina_resultado(
        "1.2 Inverso aditivo",
        resultado
    )


# ============================================================
# 1.3 INVERSO XOR
# ============================================================

@app.get("/modular/inverso-xor",
         response_class=HTMLResponse)
def pagina_inverso_xor():

    return formulario_base(
        "1.3 Inverso XOR",
        "Realiza XOR entre dos valores y comprueba la reversibilidad.",
        [
            {
                "name": "a",
                "label": "Valor a"
            },
            {
                "name": "b",
                "label": "Valor b"
            }
        ],
        "/modular/inverso-xor"
    )


@app.post("/modular/inverso-xor",
          response_class=HTMLResponse)
def calcular_inverso_xor(
    a: int = Form(...),
    b: int = Form(...)
):

    xor = a ^ b
    recuperado = xor ^ b

    resultado = f"""
    <div class="result">

        <h2>Resultado</h2>

        <div class="formula">
            {a} XOR {b} = {xor}
        </div>

        <p>
            Aplicando XOR nuevamente:
        </p>

        <div class="formula">
            {xor} XOR {b} = {recuperado}
        </div>

        <p class="success">
            ✓ Se recupera el valor original:
            {recuperado} = {a}
        </p>

    </div>
    """

    return pagina_resultado(
        "1.3 Inverso XOR",
        resultado
    )


# ============================================================
# 1.4 MCD
# ============================================================

@app.get("/modular/mcd",
         response_class=HTMLResponse)
def pagina_mcd():

    return formulario_base(
        "1.4 MCD",
        "Calcula el máximo común divisor y determina si existe inverso multiplicativo.",
        [
            {
                "name": "a",
                "label": "Número a"
            },
            {
                "name": "n",
                "label": "Módulo n",
                "extra": "min='1'"
            }
        ],
        "/modular/mcd"
    )


@app.post("/modular/mcd",
          response_class=HTMLResponse)
def calcular_mcd(
    a: int = Form(...),
    n: int = Form(...)
):

    import math

    if n <= 0:

        resultado = """
        <div class="error">
            El módulo n debe ser mayor que 0.
        </div>
        """

    else:

        mcd = math.gcd(a, n)

        if mcd == 1:

            inverso = pow(a, -1, n)

            resultado = f"""
            <div class="result">

                <h2>Resultado</h2>

                <div class="formula">
                    MCD({a}, {n}) = 1
                </div>

                <p class="success">
                    ✓ Existe inverso multiplicativo.
                </p>

                <div class="formula">
                    Inverso = {inverso}
                </div>

            </div>
            """

        else:

            resultado = f"""
            <div class="result">

                <h2>Resultado</h2>

                <div class="formula">
                    MCD({a}, {n}) = {mcd}
                </div>

                <p class="danger">
                    ✗ No existe inverso multiplicativo
                    porque el MCD no es 1.
                </p>

            </div>
            """

    return pagina_resultado(
        "1.4 MCD",
        resultado
    )


# ============================================================
# 1.5 INVERSO MULTIPLICATIVO TRADICIONAL
# ============================================================

@app.get("/modular/inverso-tradicional",
         response_class=HTMLResponse)
def pagina_inverso_tradicional():

    return formulario_base(
        "1.5 Inverso multiplicativo tradicional",
        "Busca un número x tal que (a × x) mod n = 1.",
        [
            {
                "name": "a",
                "label": "Número a"
            },
            {
                "name": "n",
                "label": "Módulo n",
                "extra": "min='2'"
            }
        ],
        "/modular/inverso-tradicional"
    )


@app.post("/modular/inverso-tradicional",
          response_class=HTMLResponse)
def calcular_inverso_tradicional(
    a: int = Form(...),
    n: int = Form(...)
):

    if n < 2:

        resultado = """
        <div class="error">
            El módulo n debe ser mayor o igual a 2.
        </div>
        """

    else:

        inverso = None
        intentos = []

        for x in range(1, n):

            valor = (a * x) % n

            intentos.append(
                f"{a} × {x} mod {n} = {valor}"
            )

            if valor == 1:
                inverso = x
                break

        if inverso is not None:

            filas = ""

            for intento in intentos:
                filas += f"""
                <tr>
                    <td>{intento}</td>
                </tr>
                """

            resultado = f"""
            <div class="result">

                <h2>Resultado</h2>

                <p>
                    Se encontró el valor:
                </p>

                <div class="formula">
                    x = {inverso}
                </div>

                <p class="success">
                    ✓ {a} × {inverso} mod {n} = 1
                </p>

                <h3>Proceso</h3>

                <div class="table-container">

                    <table>

                        <tr>
                            <th>Intento</th>
                        </tr>

                        {filas}

                    </table>

                </div>

            </div>
            """

        else:

            resultado = f"""
            <div class="error">

                <h2>No existe inverso</h2>

                <p>
                    No se encontró ningún x entre 1 y {n - 1}
                    que cumpla:
                </p>

                <div class="formula">
                    ({a} × x) mod {n} = 1
                </div>

            </div>
            """

    return pagina_resultado(
        "1.5 Inverso tradicional",
        resultado
    )


# ============================================================
# 1.6 ALGORITMO EXTENDIDO DE EUCLIDES
# ============================================================

@app.get("/modular/aee",
         response_class=HTMLResponse)
def pagina_aee():

    return formulario_base(
        "1.6 Algoritmo Extendido de Euclides",
        "Calcula el inverso multiplicativo mediante AEE y muestra la tabla de rondas.",
        [
            {
                "name": "a",
                "label": "Número a"
            },
            {
                "name": "n",
                "label": "Módulo n",
                "extra": "min='2'"
            }
        ],
        "/modular/aee"
    )


@app.post("/modular/aee",
          response_class=HTMLResponse)
def calcular_aee(
    a: int = Form(...),
    n: int = Form(...)
):

    if n < 2:

        resultado = """
        <div class="error">
            El módulo n debe ser mayor o igual a 2.
        </div>
        """

        return pagina_resultado(
            "1.6 AEE",
            resultado
        )

    original_a = a
    original_n = n

    # Para el cálculo del inverso se trabaja
    # con valores positivos.
    a_actual = a
    n_actual = n

    # Algoritmo de Euclides
    r0 = a_actual
    r1 = n_actual

    # Coeficientes de Bézout
    t0 = 1
    t1 = 0

    tabla = []
    ronda = 0

    while r1 != 0:

        cociente = r0 // r1
        resto = r0 % r1

        tabla.append({
            "ronda": ronda + 1,
            "r0": r0,
            "r1": r1,
            "q": cociente,
            "r": resto,
            "t0": t0,
            "t1": t1
        })

        nuevo_t = t0 - cociente * t1

        r0 = r1
        r1 = resto

        t0 = t1
        t1 = nuevo_t

        ronda += 1

    mcd = abs(r0)

    if mcd != 1:

        filas = ""

        for fila in tabla:

            filas += f"""
            <tr>
                <td>{fila['ronda']}</td>
                <td>{fila['r0']}</td>
                <td>{fila['r1']}</td>
                <td>{fila['q']}</td>
                <td>{fila['r']}</td>
            </tr>
            """

        resultado = f"""
        <div class="result">

            <h2>Resultado</h2>

            <div class="formula">
                MCD({original_a}, {original_n}) = {mcd}
            </div>

            <p class="danger">
                ✗ No existe inverso multiplicativo
                porque el MCD no es 1.
            </p>

            <h3>Tabla de rondas</h3>

            <div class="table-container">

                <table>

                    <tr>
                        <th>Ronda</th>
                        <th>r₀</th>
                        <th>r₁</th>
                        <th>q</th>
                        <th>r</th>
                    </tr>

                    {filas}

                </table>

            </div>

        </div>
        """

    else:

        inverso = t0 % original_n

        filas = ""

        for fila in tabla:

            filas += f"""
            <tr>
                <td>{fila['ronda']}</td>
                <td>{fila['r0']}</td>
                <td>{fila['r1']}</td>
                <td>{fila['q']}</td>
                <td>{fila['r']}</td>
            </tr>
            """

        resultado = f"""
        <div class="result">

            <h2>Resultado</h2>

            <div class="formula">
                MCD({original_a}, {original_n}) = 1
            </div>

            <p class="success">
                ✓ Existe inverso multiplicativo.
            </p>

            <div class="formula">
                Inverso de {original_a}
                módulo {original_n}
                = {inverso}
            </div>

            <p>
                Rondas realizadas:
                <strong>{len(tabla)}</strong>
            </p>

            <h3>Tabla del Algoritmo Extendido de Euclides</h3>

            <div class="table-container">

                <table>

                    <tr>
                        <th>Ronda</th>
                        <th>r₀</th>
                        <th>r₁</th>
                        <th>q</th>
                        <th>r</th>
                    </tr>

                    {filas}

                </table>

            </div>

            <h3>Comprobación</h3>

            <div class="formula">
                ({original_a} × {inverso})
                mod {original_n}
                = {(original_a * inverso) % original_n}
            </div>

        </div>
        """

    return pagina_resultado(
        "1.6 AEE",
        resultado
    )


# ============================================================
# PÁGINA DE RESULTADO
# ============================================================

def pagina_resultado(titulo, resultado):

    return f"""
    <!DOCTYPE html>

    <html lang="es">

    <head>

        <meta charset="UTF-8">

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>{titulo}</title>

        {STYLE}

    </head>

    <body>

        <div class="small-container">

            <a href="/modular">
                ← Volver a Matemática Modular
            </a>

            {resultado}

            <div class="actions">

                <a class="btn"
                   href="/modular">
                    Volver al menú
                </a>

            </div>

        </div>

    </body>

    </html>
    """


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "application": "Calculadora Criptográfica"
    }