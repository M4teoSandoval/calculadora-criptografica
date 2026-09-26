
import app


# ============================================================
#                 FUNCIONES AUXILIARES
# ============================================================

def pausar():
    input("\nPresione ENTER para continuar...")


def leer_entero(mensaje):
    """Pide un entero. Si el usuario escribe otra cosa devuelve None."""
    try:
        return int(input(mensaje))
    except ValueError:
        print("Error: debe ingresar números enteros.")
        return None


# ============================================================
#              1. MATEMÁTICA MODULAR
# ============================================================

def calcular_modulo():
    print("\n--- 1.1 CALCULAR MÓDULO ---")

    a = leer_entero("Ingrese el valor de a: ")
    n = leer_entero("Ingrese el valor de n: ")

    if a is None or n is None:
        return

    try:
        resultado = app.calcular_modulo(a, n)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"\n{a} mod {n} = {resultado['resultado']}")


def inverso_aditivo():
    print("\n--- 1.2 INVERSO ADITIVO ---")

    a = leer_entero("Ingrese el valor de a: ")
    n = leer_entero("Ingrese el módulo n: ")

    if a is None or n is None:
        return

    try:
        resultado = app.inverso_aditivo(a, n)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(
        f"\nEl inverso aditivo de {a} módulo {n} es: "
        f"{resultado['inverso']}"
    )
    print(
        f"Comprobación: ({a} + {resultado['inverso']}) mod {n} = "
        f"{resultado['comprobacion']}"
    )


def inverso_xor():
    print("\n--- 1.3 INVERSO DE XOR ---")

    a = leer_entero("Ingrese el primer número: ")
    b = leer_entero("Ingrese el segundo número: ")

    if a is None or b is None:
        return

    resultado = app.inverso_xor(a, b)

    print(f"\n{a} XOR {b} = {resultado['resultado']}")
    print(
        f"Comprobación: {resultado['resultado']} XOR {b} = "
        f"{resultado['recuperado']}"
    )


def calcular_mcd():
    print("\n--- 1.4 MCD E INVERSO MULTIPLICATIVO ---")

    a = leer_entero("Ingrese el valor de a: ")
    n = leer_entero("Ingrese el módulo n: ")

    if a is None or n is None:
        return

    try:
        resultado = app.calcular_mcd(a, n)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"\nMCD({a}, {n}) = {resultado['mcd']}")

    if not resultado["existe_inverso"]:
        print("No existe inverso multiplicativo.")
        print("La razón es que MCD(a, n) ≠ 1.")
        return

    print("Sí existe inverso multiplicativo.")
    print(f"Inverso multiplicativo = {resultado['inverso']}")
    print(
        f"Comprobación: ({a} × {resultado['inverso']}) mod {n} = "
        f"{resultado['comprobacion']}"
    )


def inverso_multiplicativo_tradicional():
    print("\n--- 1.5 INVERSO MULTIPLICATIVO - MÉTODO TRADICIONAL ---")

    a = leer_entero("Ingrese el valor de a: ")
    n = leer_entero("Ingrese el módulo n: ")

    if a is None or n is None:
        return

    try:
        resultado = app.inverso_multiplicativo_tradicional(a, n)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    if resultado["mcd"] != 1:
        print(f"\nMCD({a}, {n}) = {resultado['mcd']}")
        print("No existe inverso multiplicativo.")
        return

    print("\nBuscando x tal que:")
    print(f"{a} × x ≡ 1 (mod {n})")
    print("\nProcedimiento:")

    for intento in resultado["intentos"]:
        print(
            f"{a} × {intento['x']} mod {n} = {intento['valor']}"
        )

    if not resultado["existe_inverso"]:
        print(
            f"\nNo se encontró ningún valor entre 1 y {n - 1} "
            f"que cumpla ({a} × x) mod {n} = 1."
        )
        return

    print(f"\nInverso multiplicativo = {resultado['inverso']}")
    print(
        f"Comprobación: ({a} × {resultado['inverso']}) mod {n} = "
        f"{(a * resultado['inverso']) % n}"
    )


def inverso_multiplicativo_aee():
    print("\n--- 1.6 INVERSO MULTIPLICATIVO - AEE ---")

    a = leer_entero("Ingrese el valor de a: ")
    n = leer_entero("Ingrese el módulo n: ")

    if a is None or n is None:
        return

    try:
        resultado = app.inverso_multiplicativo_aee(a, n)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"\nMCD({a}, {n}) = {resultado['mcd']}")

    if not resultado["existe_inverso"]:
        print("No existe inverso multiplicativo.")
        return

    print(f"Rondas del algoritmo: {resultado['rondas']}")

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

    for fila in resultado["tabla"]:
        print(
            f"{fila['ronda']:<8}"
            f"{fila['r_anterior']:<15}"
            f"{fila['r_actual']:<15}"
            f"{fila['cociente']:<12}"
            f"{fila['residuo']:<12}"
        )

    print("-" * 75)

    print(f"\nInverso multiplicativo = {resultado['inverso']}")

    print(
        f"Comprobación: ({a} × {resultado['inverso']}) mod {n} = "
        f"{resultado['comprobacion']}"
    )


# ============================================================
#              2. CRIPTOGRAFÍA CLÁSICA
# ============================================================

def modulo_27():
    print("\n--- 2.1 CIFRADO MÓDULO 27 ---")

    texto = input("Ingrese el texto: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))

    resultado = app.modulo_27(texto, desplazamiento)

    print(f"\nTexto original: {resultado['texto']}")
    print(f"Texto cifrado:  {resultado['resultado']}")


def cesar():
    print("\n--- 2.2 CIFRADO CÉSAR ---")

    texto = input("Ingrese el texto: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))
    opcion = input("¿Desea cifrar o descifrar? (C/D): ").upper()

    resultado = app.cesar(texto, desplazamiento, opcion == "D")

    print(f"\nResultado: {resultado['resultado']}")


def vernam():
    print("\n--- 2.3 CIFRADO VERNAM ---")

    texto = input("Ingrese el texto: ")
    clave = input("Ingrese la clave: ")

    try:
        resultado = app.vernam(texto, clave)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"\nTexto:  {resultado['texto']}")
    print(f"Clave:  {resultado['clave']}")
    print(f"Resultado: {resultado['resultado']}")


def atbash():
    print("\n--- 2.4 CIFRADO ATBASH ---")

    texto = input("Ingrese el texto: ")

    resultado = app.atbash(texto)

    print(f"\nResultado: {resultado['resultado']}")


def transposicion_columnar():
    print("\n--- 2.5 TRANSPOSICIÓN COLUMNAR SIMPLE ---")

    texto = input("Ingrese el texto: ")
    clave = input("Ingrese la clave (palabra): ")

    try:
        resultado = app.transposicion_columnar(texto, clave)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"\nClave: {resultado['clave']}")
    print(f"Número de columnas: {resultado['columnas']}")
    print(f"Filas: {resultado['filas']}")
    print(f"Orden de lectura: {'  '.join(resultado['orden_lectura'])}")

    print("\nMatriz:")

    for fila in resultado["matriz"]:
        print("  ".join(fila.values()))

    print(f"\nTexto cifrado: {resultado['resultado']}")


def afin():
    print("\n--- 2.6 CIFRADO AFÍN ---")

    texto = input("Ingrese el texto: ")
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    opcion = input("¿Desea cifrar o descifrar? (C/D): ").upper()

    try:
        resultado = app.afin(texto, a, b, opcion)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"\nResultado: {resultado['resultado']}")


def sustitucion_simple():
    print("\n--- 2.7 CIFRA DE SUSTITUCIÓN SIMPLE ---")

    clave = input(
        "Ingrese el alfabeto de sustitución (26 letras): "
    )
    texto = input("Ingrese el texto: ")
    opcion = input("¿Desea cifrar o descifrar? (C/D): ").upper()

    try:
        resultado = app.sustitucion_simple(texto, clave, opcion)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"\nResultado: {resultado['resultado']}")


# ============================================================
#              3. CRIPTOGRAFÍA MODERNA
# ============================================================

def diffie_hellman():
    print("\n--- 3.1 DIFFIE-HELLMAN ---")

    p = int(input("Ingrese un número primo p: "))
    g = int(input("Ingrese la raíz primitiva g: "))
    a = int(input("Ingrese la clave privada de Alice: "))
    b = int(input("Ingrese la clave privada de Bob: "))

    resultado = app.diffie_hellman(p, g, a, b)

    print("\n--- RESULTADOS ---")
    print(
        f"Clave pública de Alice: {resultado['publica_alice']}"
    )
    print(f"Clave pública de Bob:   {resultado['publica_bob']}")
    print(
        f"Clave calculada por Alice: {resultado['clave_alice']}"
    )
    print(
        f"Clave calculada por Bob:   {resultado['clave_bob']}"
    )

    if resultado["coinciden"]:
        print("\nIntercambio exitoso.")
        print(f"Clave compartida: {resultado['clave_alice']}")


def rsa():
    print("\n--- 3.2 RSA ---")

    p = int(input("Ingrese el número primo p: "))
    q = int(input("Ingrese el número primo q: "))

    parametros = app.criptografia_moderna.rsa_parametros(p, q)
    n = parametros["n"]
    phi = parametros["phi"]

    print(f"\nn = p × q = {n}")
    print(f"φ(n) = {phi}")

    e = int(input("Ingrese e: "))

    try:
        claves = app.criptografia_moderna.rsa_clave_privada(p, q, e)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"Clave pública: {claves['clave_publica']}")
    print(f"Clave privada: {claves['clave_privada']}")

    mensaje = int(input(f"Ingrese el mensaje como número menor que {n}: "))

    try:
        resultado = app.rsa(p, q, e, mensaje)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print(f"\nMensaje original: {resultado['mensaje']}")
    print(f"Mensaje cifrado: {resultado['cifrado']}")
    print(f"Mensaje descifrado: {resultado['descifrado']}")


def exponenciacion_rapida():
    print("\n--- 3.3 EXPONENCIACIÓN RÁPIDA ---")

    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    modulo = int(input("Ingrese el módulo: "))

    try:
        resultado = app.exponenciacion_rapida(base, exponente, modulo)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print("\nProcedimiento:")
    print("-" * 60)

    for ronda in resultado["rondas"]:
        print(
            f"Ronda {ronda['ronda']}: "
            f"resultado={ronda['resultado']}, "
            f"base={ronda['base']}, "
            f"exponente={ronda['exponente']}"
        )

    print("-" * 60)
    print(
        f"\nResultado: {resultado['base']}^{resultado['exponente']} "
        f"mod {resultado['modulo']} = {resultado['resultado']}"
    )


# ============================================================
#                     4. HASH
# ============================================================

def hash_md5():
    print("\n--- 4.1 MD5 ---")

    texto = input("Ingrese el texto: ")

    resultado = app.hash_md5(texto)

    print(f"\nTexto: {resultado['texto']}")
    print(f"MD5:   {resultado['hash']}")


def hash_sha256():
    print("\n--- 4.2 SHA-256 ---")

    texto = input("Ingrese el texto: ")

    resultado = app.hash_sha256(texto)

    print(f"\nTexto:   {resultado['texto']}")
    print(f"SHA-256: {resultado['hash']}")


def hash_sha512():
    print("\n--- 4.3 SHA-512 ---")

    texto = input("Ingrese el texto: ")

    resultado = app.hash_sha512(texto)

    print(f"\nTexto:   {resultado['texto']}")
    print(f"SHA-512: {resultado['hash']}")


# ============================================================
#                   5. CODIFICACIÓN
# ============================================================

def codificacion_ascii():
    print("\n--- 5.1 ASCII ---")

    opcion = input("¿Desea codificar o decodificar? (C/D): ").upper()

    if opcion == "C":
        texto = input("Ingrese el texto: ")
        resultado = app.ascii_codificar(texto)

    elif opcion == "D":
        valores = input(
            "Ingrese los valores ASCII separados por espacios: "
        )
        resultado = app.ascii_decodificar(valores)

    else:
        resultado = None

    if resultado is None:
        print(app.mensaje_error(ValueError("Opción no válida.")))
        return

    print(f"\n{resultado['etiqueta']}: {resultado['salida']}")


def codificacion_hexadecimal():
    print("\n--- 5.2 HEXADECIMAL ---")

    opcion = input("¿Desea codificar o decodificar? (C/D): ").upper()

    if opcion == "C":
        texto = input("Ingrese el texto: ")
        resultado = app.hexadecimal_codificar(texto)

    elif opcion == "D":
        hexadecimal = input("Ingrese el hexadecimal: ")
        resultado = app.hexadecimal_decodificar(hexadecimal)

    else:
        resultado = None

    if resultado is None:
        print(app.mensaje_error(ValueError("Opción no válida.")))
        return

    print(f"\n{resultado['etiqueta']}: {resultado['salida']}")


def codificacion_binario():
    print("\n--- 5.3 BINARIO ---")

    opcion = input("¿Desea codificar o decodificar? (C/D): ").upper()

    if opcion == "C":
        texto = input("Ingrese el texto: ")
        resultado = app.binario_codificar(texto)

    elif opcion == "D":
        binario = input(
            "Ingrese los valores binarios separados por espacios: "
        )
        resultado = app.binario_decodificar(binario)

    else:
        resultado = None

    if resultado is None:
        print(app.mensaje_error(ValueError("Opción no válida.")))
        return

    print(f"\n{resultado['etiqueta']}: {resultado['salida']}")


def codificacion_base64():
    print("\n--- 5.4 BASE64 ---")

    opcion = input("¿Desea codificar o decodificar? (C/D): ").upper()

    if opcion == "C":
        texto = input("Ingrese el texto: ")
        resultado = app.base64_codificar(texto)

    elif opcion == "D":
        texto = input("Ingrese el texto Base64: ")
        resultado = app.base64_decodificar(texto)

    else:
        resultado = None

    if resultado is None:
        print(app.mensaje_error(ValueError("Opción no válida.")))
        return

    print(f"\n{resultado['etiqueta']}: {resultado['salida']}")


# ============================================================
#                        6. SALT
# ============================================================

def hash_con_salt(algoritmo):
    print(f"\n--- HASH {algoritmo.upper()} CON SALT ---")

    clave = input("Ingrese la clave: ")
    cantidad = int(
        input("¿Cuántos SALT diferentes desea generar?: ")
    )

    try:
        resultado = app.hash_con_salt(clave, algoritmo, cantidad)
    except ValueError as error:
        print(app.mensaje_error(error))
        return

    print("\n" + "=" * 80)

    for item in resultado["resultados"]:
        print(f"\nSALT {item['numero']}: {item['salt']}")
        print(f"HASH:   {item['hash']}")

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
