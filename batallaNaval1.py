import random

def crearTablero(dimension):
    return [["~" for _ in range(dimension)] for _ in range(dimension)]

def mostrartTableros(tableroDisparoJugador, tableroDisparosOponentes):
    print("\n Tablero de disparos: ")
    for fila in tableroDisparoJugador:
        print(" ".join(fila))
    print("\n Tablero de disparos del oponente: ")
    for fila in tableroDisparosOponentes:
        print(" ".join(fila))

def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado: False
        while not colocado:
            if jugador == "jugador":
                print(f"Colocado {barco ['nombre']} de tamaño {barco['dimension']}")
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna: "))
                orientacion = int(input("Ingrese la orientación (h para horizontal, v para vertical): ")).lower()
                
                if validarColocado(tablero, fila, columna, barco['dimension'], orientacion):
                    colocarBarcos(tablero, fila, columna, barco['dimension'], orientacion)
                    colocado = True
                elif jugador == "jugador":
                    print("Colocación invalida. Intente de nuevo")
    