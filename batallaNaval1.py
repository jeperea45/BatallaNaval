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
                    
def validarColocado(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        if columna + dimension > len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila][columna+i] != "~":
                return False
    else:
        if fila + dimension > len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila+i][columna] != "~":
                return False
    return True

def colocarBarco(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        for i in range(dimension):
            tablero[fila][columna+i] = "B"
    else:
        for i in range(dimension):
            tablero[fila+i][columna] = "B"
            
def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] == "X"
        tableroOculto[fila][columna] == "H"
        return "Impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroOculto[fila][columna] == "O"
        return "Agua"
    return "Ya disparaste aquí"
    
def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:
            return False
    return True
            
def jugarContraComputadora():
    dimension = 5
    tableroJugador = crearTablero(dimension)
    tableroComputadora = crearTablero(dimension)
    tableroDisparosJugador = crearTablero(dimension)
    tableroDisparosComputadora = crearTablero(dimension)
    barcos = [
        {"nombre": "PortaAviones", "dimension": 3},
        {"nombre": "SubMarino", "dimension": 2}
    ]
    print("Coloca tus barcos")
    colocarBarcos(tableroJugador, barcos, "Jugador")
    colocarBarcos(tableroComputadora, barcos, "Computadora")
    turnoJugador = True
    while True:
        if turnoJugador:
            print("\nTu turno")
            mostrartTableros(tableroDisparosJugador, tableroDisparosComputadora)
            fila = int(input("Ingrese la fila de disparo: "))
            columna = int(input("Ingresa la columna de disparo: "))
            resultado = realizarDisparo(tableroComputadora, tableroDisparosJugador, fila, columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("Ganaste")
                return "Jugador"
        else:
            print("\n Turno de la computadora")
            fila = random.radiant(0, dimension -1)
            columna = random.radiant(0, dimension -1)
            resultado = realizarDisparo(tableroJugador, tableroDisparosComputadora, fila, columna)
            print(f"La computadora disparo en ({fila}, {columna}): {resultado} ")
            if verificarVictoria(tableroJugador):
                print("La computadora gano")
                return "Computadora"
    turnoJugador = not turnoJugador