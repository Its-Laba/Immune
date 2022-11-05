"""
    RETO LABERINTO (Pintar el laberinto y resolverlo)
"""


def crear_maze(muros, dimension):

#   muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

    laberinto = []
    for i in range(dimension):
        laberinto.append(list(range(dimension)))
    for fila in laberinto:
        for num, columna in enumerate(fila):
            fila[num] = " "

    for muro in muros:
        fila = muro[0]
        columna = muro[1]
        laberinto[fila][columna] = "X"

    laberinto[0][0] = "E"
    laberinto[dimension-1][dimension-1] = "S"
    return laberinto


def print_maze(laberinto):
    for fila in laberinto:
        print(fila)


def casillas_posibles(pos, dim=5):
    posibles = [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]

    reales = []

    for pos in posibles:
        if (pos[0] >= 0) and (pos[1] >= 0) and (pos[0] < dim) and (pos[1] < dim):
            reales.append(pos)

    return reales


def solve_maze(laberinto):
    casillas_ocupadas = []
    casilla_actual = (0,0)
    instrucciones = []

    dim = len(laberinto)

    found = False

    while not found:
        posibles = casillas_posibles(casilla_actual, dim)
        print(posibles)

        for pos in posibles:
            nextPos = laberinto[pos[0]][pos[1]]
            #print("nextPos", nextPos)
            #print("pos", pos)
            if (pos not in casillas_ocupadas) and (nextPos == " " or nextPos == "S"):
                if pos[0] > casilla_actual[0]:
                    instrucciones.append("Abajo")
                elif pos[0] < casilla_actual[0]:
                    instrucciones.append("Arriba")
                elif pos[1] > casilla_actual[1]:
                    instrucciones.append("Derecha")
                elif pos[1] < casilla_actual[1]:
                    instrucciones.append("Izquierda")

                casillas_ocupadas.append(casilla_actual)
                casilla_actual = (pos[0], pos[1])


            if nextPos == "S":
                found = True



    return instrucciones


# muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))
# laberinto = crear_maze(muros,5)
#
# print(solve_maze(laberinto))
#
# print_maze(laberinto)

def solucionar_maze():
    print("----------------------------------")
    pos = solucion[len(solucion)-1]
    if pos == (len(maze)-1, len(maze)-1):
        return

    fila = pos[0]
    columna = pos[1]

    if fila + 1 < len(maze) and (maze[fila+1][columna] == " " or maze[fila+1][columna] == "S"):
        maze[fila+1][columna] = "|"
        solucion.append((fila+1, columna))
        print_maze(maze)
        solucionar_maze()
    if columna + 1 < len(maze[fila]) and (maze[fila][columna+1] == " " or maze[fila][columna+1] == "S"):
        maze[fila][columna+1] = "-"
        solucion.append((fila, columna+1))
        print_maze(maze)
        solucionar_maze()
    if fila - 1 >= 0 and (maze[fila-1][columna] == " " or maze[fila-1][columna] == "S"):
        maze[fila-1][columna] = "|"
        solucion.append((fila-1, columna))
        print_maze(maze)
        solucionar_maze()
    if columna - 1 >= 0 and (maze[fila][columna-1] == " " or maze[fila][columna-1] == "S"):
        maze[fila][columna+1] = "-"
        solucion.append((fila, columna-1))
        print_maze(maze)
        solucionar_maze()

    pos = solucion[len(solucion)-1]
    if pos != (len(maze)-1, len(maze)-1):
        maze[pos[0]][pos[1]] = "."
        solucion.remove(pos)


def ordenes(pasos):
    ordenes = []
    for num, paso in enumerate(pasos):
        if num == 0:
            continue
        fila = paso[0] - pasos[num-1][0]
        columna = paso[1] - pasos[num-1][1]
        if fila > 0:
            ordenes.append("Abajo")
        elif fila < 0:
            ordenes.append("Arriba")
        elif columna > 0:
            ordenes.append("Derecha")
        elif columna < 0:
            ordenes.append("Izquierda")
    return ordenes


if __name__ == "__main__":

    muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 3))
    maze = crear_maze(muros, 5)
    print_maze(maze)
    solucion = [(0, 0)]
    solucionar_maze()
    instrucciones = ordenes(solucion)
    print(instrucciones)

