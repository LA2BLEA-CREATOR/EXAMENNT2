import random

def generar_palabra():
    palabra = ""
    for i in range(4):
        letra = chr(random.randint(97, 122))
        palabra += letra
    return palabra

def generar_matriz(tamano):
    matriz = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            fila.append(generar_palabra())
        matriz.append(fila)
    return matriz

def tiene_vocal(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    for v in vocales:
        if v in palabra:
            return True
    return False

def contar_vocales_matriz(matriz):
    n = len(matriz)
    if n == 1:
        if tiene_vocal(matriz[0][0]):
            return 1
        else:
            return 0

    mitad = n // 2
    sup_izq = [fila[:mitad] for fila in matriz[:mitad]]
    sup_der = [fila[mitad:] for fila in matriz[:mitad]]
    inf_izq = [fila[:mitad] for fila in matriz[mitad:]]
    inf_der = [fila[mitad:] for fila in matriz[mitad:]]

    c1 = contar_vocales_matriz(sup_izq)
    c2 = contar_vocales_matriz(sup_der)
    c3 = contar_vocales_matriz(inf_izq)
    c4 = contar_vocales_matriz(inf_der)

    return c1 + c2 + c3 + c4

def main():
    print("=== MATRIZ DE PALABRAS ALEATORIAS ===")
    n = int(input("Ingrese el tamaño de la matriz (ejemplo: 8): "))
    matriz = generar_matriz(n)
    print("\nMatriz generada:")
    for fila in matriz:
        print(fila)
    total_con_vocal = contar_vocales_matriz(matriz)
    print("\nCantidad total de palabras con al menos una vocal:", total_con_vocal)

if __name__ == "__main__":
    main()
