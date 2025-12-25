cartas = [
"""┌────┐
│A ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│2 ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│3 ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│4 ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│5 ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│6 ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│7 ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│8 ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│9 ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│10 ♠│
│ ♠  │
└────┘""",
"""┌────┐
│J ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│Q ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│K ♠ │
│ ♠  │
└────┘""",
"""┌────┐
│A ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│2 ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│3 ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│4 ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│5 ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│6 ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│7 ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│8 ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│9 ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│10 ♥│
│ ♥  │
└────┘""",
"""┌────┐
│J ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│Q ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│K ♥ │
│ ♥  │
└────┘""",
"""┌────┐
│A ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│2 ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│3 ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│4 ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│5 ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│6 ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│7 ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│8 ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│9 ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│10 ♦│
│ ♦  │
└────┘""",
"""┌────┐
│J ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│Q ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│K ♦ │
│ ♦  │
└────┘""",
"""┌────┐
│A ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│2 ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│3 ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│4 ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│5 ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│6 ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│7 ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│8 ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│9 ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│10 ♣│
│ ♣  │
└────┘""",
"""┌────┐
│J ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│Q ♣ │
│ ♣  │
└────┘""",
"""┌────┐
│K ♣ │
│ ♣  │
└────┘"""
]

copia_mazo = cartas

carta_vacia = """┌────┐
│    │
│    │
└────┘"""

import random, time, os

def imprimir_cartas_del_jugador(cartas_jugador):
    
    print("Tus cartas son: ")
    for j in range(0, len(cartas_jugador[0])): # Se usa cero (o uno) porque es la cantidad de lineas que hay en una carta, y la conseguimos antes con el .split
        for i in range(0, len(cartas_jugador)):
            print(cartas_jugador[i][j], end = "\t")
        print("")


def imprimir_cartas_de_la_computadora(cartas_computadora):
    
    print("\nLas cartas del dealer son: ")
    for j in range(0, len(cartas_computadora[0])): 
        for i in range(0, len(cartas_computadora)):
            print(cartas_computadora[i][j], end = "\t")
        print("")


def calcular_valor(cartas):
    valor1 = 0
    valor2 = 0
    ctr_A = False

    for carta in cartas:
        if "10" in carta[1] or "J" in carta[1] or "Q" in carta[1] or "K" in carta[1]:
            valor1 += 10
            valor2 += 10
        elif "1" in carta[1]:
            valor1 += 1
            valor2 += 1
        elif "2" in carta[1]:
            valor1 += 2
            valor2 += 2
        elif "3" in carta[1]:
            valor1 += 3
            valor2 += 3
        elif "4" in carta[1]:
            valor1 += 4
            valor2 += 4
        elif "5" in carta[1]:
            valor1 += 5
            valor2 += 5
        elif "6" in carta[1]:
            valor1 += 6
            valor2 += 6
        elif "7" in carta[1]:
            valor1 += 7
            valor2 += 7
        elif "8" in carta[1]:
            valor1 += 8
            valor2 += 8
        elif "9" in carta[1]:
            valor1 += 9
            valor2 += 9
        # En Python "10" or "J" or "Q" or "K" in linea se evalúa como ("10") or ("J") or ("Q") or ("K" in linea), y como "10" es una cadena no vacía (True), toda la condición siempre resulta verdadera sin importar el contenido de linea. Entonces se debe hacer de la siguiente manera:
        elif "A" in carta[1]:
            valor1 += 1
            valor2 += 11
            ctr_A = True
        else:
            valor1 += 0
            valor2 += 0
            
    if ctr_A == True and valor2 <= 21:
        return [valor1, valor2]
    else:
        return [valor1, 0]


def mostrar_mano(cartas_jugador, valor_jugador, cartas_computadora, valor_computadora):
    if valor_jugador[1] == 0:
        imprimir_cartas_del_jugador(cartas_jugador)
        print(f"Valor del jugador: {valor_jugador[0]}")
        imprimir_cartas_de_la_computadora(cartas_computadora)
        print(f"Valor del dealer: {valor_computadora[0]}\n")
    else:
        imprimir_cartas_del_jugador(cartas_jugador)
        print(f"Valor del jugador: {valor_jugador[0]}/{valor_jugador[1]}")
        imprimir_cartas_de_la_computadora(cartas_computadora)
        print(f"Valor del dealer: {valor_computadora[0]}\n")


def juego_jugador(true_or_false, cartas_jugador, valor_jugador, cartas_computadora, valor_computadora):
    while (true_or_false):
        continuar_juego = input("Quieres pedir otra carta (h) o plantarte (p): ")
        
        if continuar_juego == "h" or continuar_juego == "H": 
            cartas_jugador.append(random.choice(cartas).split("\n"))
            valor_jugador = calcular_valor(cartas_jugador)
            time.sleep(2)
            os.system('cls')
            mostrar_mano(cartas_jugador, valor_jugador, cartas_computadora, valor_computadora)

            if valor_jugador[1] == 21:
                valor_jugador[0] = valor_jugador[1]
                true_or_false = False
            elif valor_jugador[1] == 0:
                if valor_jugador[0] == 21:
                    true_or_false = False
                elif valor_jugador[0] > 21:
                    true_or_false = False
                else:
                    continue
            
        elif continuar_juego == "p" or continuar_juego == "P":
            if valor_jugador[1] != 0:
                valor_jugador[0] = valor_jugador[1]
                valor_jugador[1] = 0
                true_or_false = False
            else:
                true_or_false = False
        else:
            print("El comando ingresado no es un comando valido.")
        
    return valor_jugador[0]


def juego_computadora(true_or_false, cartas_jugador, valor_final_jugador, cartas_computadora, valor_computadora):
    while (true_or_false):
        
        if valor_computadora[1] == 0 and valor_computadora[0] < 17: 
            cartas_computadora.append(random.choice(cartas).split("\n"))
            valor_computadora = calcular_valor(cartas_computadora)
            time.sleep(3)
            os.system('cls')
            mostrar_mano(cartas_jugador, valor_jugador, cartas_computadora, valor_computadora)

            if valor_computadora[0] == 21:
                true_or_false = False
            elif valor_computadora[0] > 21:
                print("El dealer se paso, tu ganas!")
                true_or_false = False
            else:
                continue
        
        elif valor_computadora[1] == 0 and valor_computadora[0] >= 17 and valor_computadora[0] <= 21:
            true_or_false = False
        
        elif valor_computadora[1] != 0 and valor_computadora[1] > 17 and valor_computadora[1] <= 21:
            valor_computadora[0] = valor_computadora[1]
            true_or_false = False
        
    return valor_computadora[0]


true_or_false = True

###### CONDICION PARA EMPEZAR LA PARTIDA
while(true_or_false):
    iniciar = input("Quieres jugar una partida de blackjack? (EL DEALER DEBE PLANTARSE EN 17) y/n: ")

    if iniciar == "Y" or iniciar == "y":
        break
    elif iniciar == "N" or iniciar == "n":
        true_or_false = False
    else:
        print("El comando ingresado no es un comando valido.")


###### CONDICION SI SE EMPIEZA LA PARTIDA
while(true_or_false):
    cartas_jugador = [random.choice(cartas).split("\n"), random.choice(cartas).split("\n")]
    cartas_computadora = [random.choice(cartas).split("\n"), carta_vacia.split("\n")]
    valor_jugador = calcular_valor(cartas_jugador)
    valor_computadora = calcular_valor(cartas_computadora)

    ## Primera mano
    mostrar_mano(cartas_jugador, valor_jugador, cartas_computadora, valor_computadora)

    # Juega el jugador
    valor_final_jugador = juego_jugador(true_or_false, cartas_jugador, valor_jugador, cartas_computadora, valor_computadora)
    print(f"\n--------Te has plantado en {valor_final_jugador}--------\n")
    
    true_or_false = True
    cartas_computadora.pop(1)

    # Juega la computadora y se corta el juego si el usuario ya perdio
    if valor_final_jugador <= 21:
        valor_jugador[0] = valor_final_jugador
        valor_final_computadora = juego_computadora(true_or_false, cartas_jugador, valor_jugador, cartas_computadora, valor_computadora)
    else:
        print("PERDISTE!!!!")
        break

    # Se comparan los valores del jugador y la computadora y se decide quien gana
    if valor_final_jugador > valor_final_computadora:
        print("GANASTE!!!!")
    elif valor_final_computadora > valor_final_jugador:
        print("PERDISTE!!!!")
    else:
        print("Ha sido un empate.")

    break

################################################# Terminado el 7/11/2025 en aproximadamente 5 horas ##############################################
