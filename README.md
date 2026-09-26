# Calculadora Criptográfica

Calculadora criptográfica desarrollada en Python como parte del taller de Criptografía. El proyecto reúne diferentes operaciones matemáticas, algoritmos de criptografía clásica y moderna, funciones hash, métodos de codificación y uso de SALT.

El proyecto cuenta con dos formas de interacción:

* Aplicación de consola: `calculadora.py`
* Aplicación web: interfaz desarrollada con FastAPI, HTML, CSS y JavaScript.

## Aplicación web

La calculadora se encuentra disponible en:

https://calculadora-criptografica.up.railway.app

## Funcionalidades

La aplicación contiene 26 herramientas distribuidas en 6 módulos.

### 1. Operaciones matemáticas modulares

* Cálculo de módulo
* Inverso aditivo
* Inverso mediante XOR
* MCD e inverso multiplicativo
* Inverso multiplicativo por método tradicional
* Inverso multiplicativo mediante Algoritmo Extendido de Euclides (AEE)

### 2. Criptografía clásica

* Módulo 27
* Cifrado César
* Cifrado Vernam
* Cifrado Atbash
* Transposición columnar simple
* Cifrado Afín
* Sustitución simple

### 3. Criptografía moderna

* Diffie-Hellman
* RSA
* Exponenciación rápida

### 4. Algoritmos Hash

* MD5
* SHA-256
* SHA-512

### 5. Codificación

* ASCII
* Hexadecimal
* Binario
* Base64

### 6. Uso de SALT

* MD5 con SALT
* SHA-256 con SALT
* SHA-512 con SALT

## Tecnologías utilizadas

* Python 3.11
* FastAPI
* Uvicorn
* Jinja2
* HTML
* CSS
* JavaScript

## Estructura del proyecto

```text
calculadora-criptografica/
│
├── app/
│   ├── matematica_modular.py
│   ├── criptografia_clasica.py
│   ├── criptografia_moderna.py
│   ├── hashes.py
│   ├── codificacion.py
│   └── salt.py
│
├── web/
│   ├── templates/
│   ├── static/
│   └── main.py
│
├── calculadora.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
└── .gitignore
```

## Instalación

Se requiere Python 3.11 o superior.

### 1. Clonar el repositorio

```bash
git clone https://github.com/M4teoSandoval/calculadora-criptografica.git
```

### 2. Entrar al proyecto

```bash
cd calculadora-criptografica
```

### 3. Crear un entorno virtual

En Windows:

```powershell
python -m venv venv
```

Activar el entorno virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar la versión de consola

Para ejecutar la calculadora desde la terminal:

```bash
python calculadora.py
```

El programa mostrará el menú principal con los seis módulos disponibles.

## Ejecutar la versión web localmente

Para iniciar el servidor:

```bash
python -m uvicorn web.main:app --reload
```

Luego abrir en el navegador:

```text
http://127.0.0.1:8000
```

## Despliegue

La aplicación web se encuentra desplegada en Railway.

En producción, el servidor utiliza el puerto proporcionado por Railway mediante la variable de entorno `PORT`.

Comando utilizado:

```bash
python -m uvicorn web.main:app --host 0.0.0.0 --port $PORT
```

## Repositorio

El código fuente completo del proyecto se encuentra disponible en GitHub:

https://github.com/M4teoSandoval/calculadora-criptografica

## Autor

Mateo Sandoval
