import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
# Lo primero que debemos hacer es pedirle el nombre para que el usuario se sienta identificado
puntaje = 50
iniciar_trivia = True
nombre = input("Ingrese su nombre para adentrarse en esta aventura: ")
# Palabras de bienvenida e información de sobre que va tratar la trivia a responder, con un poco de humor para que sea divertido.
print(RED +
    "\nHola "
    '\033[1m', nombre.upper(), '\033[0m' + RED+
    " hoy te toca ser médico ♥ (solo lo básico no el que estudia 7 años :D)"+ RESET)
time.sleep(3)
print(BLACK +
    "\nEmpiezas con ", puntaje,
    "puntos no te olvides que las respuestas incorrectas descuentan puntos, así que con mucho cuidado que de ti depende una vida xD." + RESET
)
time.sleep(5)

# Instrucciones para empezar el juego, sin tanto rodeos.
print(
    YELLOW+"\n=========================== INSTRUCCIONES ==========================="+RESET)
print(
  YELLOW+"Escribes la letra, presionas Enter y que empiece la diversión, éxitos :)" +RESET)
time.sleep(3)

# while para iniciar trivia y terminar si se desea.
while iniciar_trivia == True:
    puntaje = 50
    # Pregunta 1
    print(GREEN +
          "\n=====================  PREGUNTA N° 1  =====================" +
          RESET)
    print(MAGENTA +"1. ¿De qué se ocupa la otorrinolaringología?"+ RESET)
    print("a) Relacionado al oido, nariz y garganta.")
    print("b) Relacionado al corazón.")
    print("c) Relacionado al higado.")
    print("d) Relacionado a los pulmones.")

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta1 = input("\nTu respuesta: ")

    while respuesta1 not in ("a", "b", "c", "d", "x"):
        respuesta1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta1 == 'x':
        puntaje += 100
        print(
            '\n!!!Encontraste el camino secreto, te llevas 100 puntos extras¡¡¡'
        )
    elif respuesta1 == 'a':
        puntaje += 10
        print(GREEN+ '\n!Respuesta Correcta¡'+ RESET)
        print(
            YELLOW+ '\nSu ámbito es tan amplio que cuenta con al menos seis subespecialidades' +RESET
        )
    else:
        puntaje -= 10
        print( RED +
            '\nRespuesta Incorrecta :(. La otorrinolaringología está relacionado al oido, nariz y garganta.' + RESET
        )
        print(
            YELLOW + '\nSu ámbito es tan amplio que cuenta con al menos seis subespecialidades' + RESET
        )

    time.sleep(5)
    print( BLACK +'\nTu puntaje actual es: ', puntaje, RESET)

    # Pregunta 2
    print(GREEN +
          "\n=====================  PREGUNTA N° 2  =====================" +
          RESET)
    print(MAGENTA + "2. ¿Cómo se conoce al virus de inmunodeficiencia humana?" + RESET)
    print("a) VIRINH")
    print("b) VIH")
    print("c) VINHU")
    print("d) VHI")

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta2 = input("\nTu respuesta: ")
    while respuesta2 not in ("a", "b", "c", "d", "x"):
        respuesta2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta2 == 'b':
        print(GREEN+ '\n!Respuesta Correcta¡'+ RESET)
        puntaje += 10
    else:
        puntaje -= 10
        print( RED +
            '\n Respuesta Incorrecta. El virus de inmunodeficiencia humana más conocida como VIH.' + RESET
        )

    print(YELLOW + 
        '\nEl VIH es el virus que causa el SIDA y es de rápida propagación en las relaciones sexuales.' + RESET
    )

    time.sleep(5)
    print( BLACK +'\nTu puntaje actual es: ', puntaje, RESET)

    # Pregunta 3
    print(GREEN +
          "\n=====================  PREGUNTA N° 3  =====================" +
          RESET)
    print(MAGENTA+ "3. ¿Una enfermedad hepática se refiere a fallas en…?" + RESET)
    print("a) El hipotálamo.")
    print("b) Las neuronas")
    print("c) El hígado")
    print("d) El riñón")

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta3 = input("\nTu respuesta: ")
    while respuesta3 not in ("a", "b", "c", "d", "x"):
        respuesta3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta3 == 'c':
        print(GREEN+ '\n!Respuesta Correcta¡'+ RESET)
        puntaje += 10
    else:
        puntaje -= 10
        print( RED +
            '\n Respuesta Incorrecta. "hepa" hace referencia al hígado, por ejemplo, hepatitis, hepática, hepatólogo, etc.' + RESET
        )

    print( YELLOW+ 
        '\nLas personas que ingieren alcohol están más expuestas a esta afección.' + RESET
    )

    time.sleep(5)
    print( BLACK +'\nTu puntaje actual es: ', puntaje, RESET)

    # Pregunta 4
    print(GREEN +
          "\n=====================  PREGUNTA N° 4  =====================" +
          RESET)
    print(MAGENTA + "4. ¿Qué función cumple el analgésico?" + RESET)
    print("a) Desinflamar.")
    print("b) Mitigar y desaparecer el dolor.")
    print("c) Desinfectar.")
    print("d) Curar.")

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta4 = input("\nTu respuesta: ")
    while respuesta4 not in ("a", "b", "c", "d", "x"):
        respuesta4 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta4 == 'b':
        print(GREEN+ '\n!Respuesta Correcta¡'+ RESET)
        puntaje += 10
    else:
        puntaje -= 10
        print( RED +
            '\n Respuesta Incorrecta. Los analgésicos sirver para ayudar con el dolor.' +RESET
        )

    print( YELLOW + '\nLos analgésicos son recetados para combatir el dolor.' + RESET)

    time.sleep(5)
    print( BLACK +'\nTu puntaje actual es: ', puntaje, RESET)

    # Pregunta 5
    print(GREEN +
          "\n=====================  PREGUNTA N° 5  =====================" +
          RESET)
    print(MAGENTA + "5. Bazo se refiere a…" + RESET)
    print("a) Una infección.")
    print("b) Un órgano.")
    print("c) Una célula.")
    print("d) Un malestar.")

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta5 = input("\nTu respuesta: ")
    while respuesta5 not in ("a", "b", "c", "d", "x"):
        respuesta5 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta5 == 'b':
        print(GREEN+ '\n!Respuesta Correcta¡'+ RESET)
        puntaje += 10
    else:
        puntaje -= 10
        print( RED +'\n Respuesta Incorrecta. "BAZO", no vaso, es un órgano.'+ RESET)

    print(YELLOW +
        '\nBazo se refiere a un órgano. Su parónimo es vaso (términos con escritura similar y diferentes significados).' + RESET
    )

    time.sleep(5)

    if puntaje <= 80:
        print(BLACK + '\nMuy bien, obtuviste ', puntaje,
              ', yo sé que puedes más     !vamos¡' +RESET)
    else:
        print( BLACK+ '\nMuy bien, obtuviste ', puntaje, ', eres el mejor médico' + RESET)

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )
    if repetir_trivia != "si":  # != significa "distinto"
        print( YELLOW + 
            '\nMuchas gracias por jugar, espero hayas aprendido y disfrutado de la trivia de la salud.' + RESET
        )
        print( YELLOW + 'Psdt: no te olvides tomar agua y comer mucha fibra' + RESET)
        iniciar_trivia = False
