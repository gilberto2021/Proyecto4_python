print("Bienvenido al juego de preguntas")
pregunta1 = input("¿Quieres ir a la izquierda o derecha?. Escribe 'izquierda' o 'derecha'").lower()

if pregunta1 == 'izquierda':
    print("Respuesta erronea. Te has caido en un agujero y has perdido. Puedes volver a intentarlo")
else:
    pregunta2 = input("Tienes que cruzar a una isla. ¿Quieres ir nadando o esperar un barco para cruzar?. Escribe 'nadar' o 'esperar'").lower()
    if pregunta2 == 'nadar':
        print("Respuesta erronea, había tiburones. Has perdido, puedes volver a intentarlo")
    else:
        pregunta3 = input("Has llegado a una casa con 3 puertas, una puerta azul, otra roja y otra verde. ¿Cual puerta quieres abrir?. Escribe 'rojo', 'azul' o 'verde'")
        pregunta3 = pregunta3.lower()
        if pregunta3 == 'rojo' or pregunta3 == 'azul':
            print("Respuesta erronea. Has perdido. Puedes volver a intentarlo")
        else:
            print("Felicidades has ganado el juego")
