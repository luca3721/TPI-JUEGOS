import random

def generar_matriz(filas, columnas):
    return [[random.randint(1, 10) for _ in range(columnas)] for _ in range(filas)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def juego_suma_matriz():
    filas = 3
    columnas = 3
    matriz = generar_matriz(filas, columnas)
    imprimir_matriz(matriz)
    
    suma = 0
    
    for fila in matriz:
        for valor in fila:
            suma += valor
    
    intento = int(input(f"¿Cuál es la suma de todos los números en la matriz de {filas}x{columnas}? "))
    
    if intento == suma:
        print("¡Correcto!")
    else:
        print(f"¡Incorrecto! La suma correcta es {suma}.")

juego_suma_matriz()