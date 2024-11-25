import random

filas = 5
columnas = 5
minas = 5

tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

minas_colocadas = 0
while minas_colocadas < minas:
    fila = random.randint(0, filas - 1)
    columna = random.randint(0, columnas - 1)
    if tablero[fila][columna] != 'M':         tablero[fila][columna] = 'M'
    minas_colocadas += 1

for i in range(filas):
    for j in range(columnas):
        if tablero[i][j] == 'M':
            continue
        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0 <= i + x < filas and 0 <= j + y < columnas:
                    if tablero[i + x][j + y] == 'M':
                        tablero[i][j] += 1

filas = len(tablero)
columnas = len(tablero[0])
for i in range(filas):
    for j in range(columnas):
        print('?', end=" ")
        print()

revelado = [[False for _ in range(columnas)] for _ in range(filas)]

# Jugar
while True:
    try:
        fila, columna = map(int, input("Introduce fila y columna (separados por espacio): ").split())
    except ValueError:
        print("Entrada inválida. Intenta de nuevo.")
        continue

    if not (0 <= fila < filas and 0 <= columna < columnas):
        print("Coordenadas fuera del tablero. Intenta de nuevo.")
        continue

    if tablero[fila][columna] == 'M':
        print("¡Perdiste! Has pisado una mina.")
        for i in range(filas):
            for j in range(columnas):
                if tablero[i][j] == 'M':
                    print('M', end=" ")  # Mina
                else:
                    print(tablero[i][j], end=" ")
                    print()
        break

    to_reveal = [(fila, columna)]
    while to_reveal:
        x, y = to_reveal.pop()
        if revelado[x][y]:
            continue
        revelado[x][y] = True

        if tablero[x][y] == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < filas and 0 <= y + dy < columnas:
                        to_reveal.append((x + dx, y + dy))

for i in range(filas):
    for j in range(columnas):
        if revelado[i][j]:
            print(tablero[i][j], end=" ")
        else:
            print('?', end=" ")
    print()
if all(revelado[i][j] or tablero[i][j] == 'M' for i in range(filas) for j in range(columnas)):
    print("¡Felicidades, has ganado!")