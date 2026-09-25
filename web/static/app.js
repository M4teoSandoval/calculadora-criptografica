/* ============================================================
   Calculadora Criptografica · efectos de terminal
   Sin dependencias: solo JavaScript nativo.
   ============================================================ */

(function () {
    "use strict";

    var LINEAS = [
        "[ boot ] iniciando calculadora_criptografica v1.0",
        "[  ok  ] app/matematica_modular.py ....... cargado",
        "[  ok  ] app/criptografia_clasica.py ..... cargado",
        "[  ok  ] app/criptografia_moderna.py ..... cargado",
        "[  ok  ] app/hashes.py ................... cargado",
        "[  ok  ] app/codificacion.py ............. cargado",
        "[  ok  ] app/salt.py ..................... cargado",
        "[ listo ] 26 algoritmos listos para ejecutar"
    ];

    /* ------------------------- registro inicial ------------------------ */

    function escribirRegistro() {
        var salida = document.getElementById("registro");

        if (!salida) {
            return;
        }

        var linea = 0;
        var caracter = 0;

        var cursor = document.createElement("span");
        cursor.className = "cursor";

        var textoNodo = document.createTextNode("");

        salida.textContent = "";
        salida.appendChild(textoNodo);
        salida.appendChild(cursor);

        var intervalo = setInterval(function () {
            if (linea >= LINEAS.length) {
                clearInterval(intervalo);

                salida.textContent = "";
                salida.appendChild(
                    document.createTextNode(LINEAS[LINEAS.length - 1])
                );
                salida.appendChild(cursor);

                return;
            }

            var texto = LINEAS[linea];
            caracter += 1;

            textoNodo.nodeValue = texto.slice(0, caracter);

            if (caracter >= texto.length) {
                caracter = 0;
                linea += 1;

                if (linea < LINEAS.length) {
                    salida.insertBefore(
                        document.createTextNode("\n"),
                        cursor
                    );
                    textoNodo = document.createTextNode("");
                    salida.insertBefore(textoNodo, cursor);
                    cursor.className = "cursor parpadeo";
                } else {
                    cursor.className = "cursor";
                }
            }
        }, 16);
    }

    /* ---------------------------- copiar ------------------------------ */

    function activarCopiar() {
        var botones = document.querySelectorAll("[data-copia]");

        Array.prototype.forEach.call(botones, function (boton) {
            boton.addEventListener("click", function () {
                var destino = document.getElementById(
                    boton.getAttribute("data-copia")
                );

                if (!destino) {
                    return;
                }

                var texto = destino.textContent.trim();

                if (navigator.clipboard) {
                    navigator.clipboard.writeText(texto);
                } else {
                    var area = document.createElement("textarea");
                    area.value = texto;
                    document.body.appendChild(area);
                    area.select();
                    document.execCommand("copy");
                    document.body.removeChild(area);
                }

                var anterior = boton.textContent;
                boton.textContent = "copiado";

                setTimeout(function () {
                    boton.textContent = anterior;
                }, 1400);
            });
        });
    }

    /* --------------------------- auto foco ---------------------------- */

    function enfocarPrimerCampo() {
        var campo = document.querySelector(".panel input, .panel select");

        if (campo) {
            campo.focus();
        }
    }

    document.addEventListener("DOMContentLoaded", function () {
        escribirRegistro();
        activarCopiar();
        enfocarPrimerCampo();
    });
}());
