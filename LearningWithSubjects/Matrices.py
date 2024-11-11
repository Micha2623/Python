import numpy as np

# Función para obtener la matriz
def obtener_matriz():
    while True:
        try:
            # Pedir las dimensiones
            dimensiones = input("Introduce las dimensiones de la matriz en formato 'filas,columnas' (ejemplo: 3,3): ")
            filas, columnas = map(int, dimensiones.split(','))

            # Verificar que la matriz no exceda 10x10
            if filas > 10 or columnas > 10:
                print("Error: El tamaño máximo permitido es 10x10. Intenta nuevamente.")
                continue

            if filas != columnas:
                print("La matriz debe ser cuadrada (filas = columnas).")
                continue

            matriz = []
            print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")

            # Ingresar los datos por fila
            for i in range(filas):
                while True:
                    fila = input(f"Fila {i + 1} (ingresar {columnas} números separados por coma): ")
                    datos_fila = list(map(float, fila.split(',')))

                    if len(datos_fila) != columnas:
                        print(f"Error: Debes ingresar exactamente {columnas} números en esta fila.")
                    else:
                        matriz.append(datos_fila)
                        break

            return np.array(matriz)

        except ValueError:
            print("Entrada inválida. Por favor, asegúrate de ingresar números correctamente.")


# Funciones para calcular el determinante, traspuesta, adjunta e inversa

def calcular_determinante(matriz):
    return np.linalg.det(matriz)

def calcular_traspuesta(matriz):
    return np.transpose(matriz)

def calcular_adjunta(matriz):
    cofactores = []
    for i in range(matriz.shape[0]):
        fila_cofactores = []
        for j in range(matriz.shape[1]):
            submatriz = np.delete(np.delete(matriz, i, axis=0), j, axis=1)
            cofactor = ((-1) ** (i + j)) * np.linalg.det(submatriz)
            fila_cofactores.append(cofactor)
        cofactores.append(fila_cofactores)
    return np.transpose(cofactores)

def calcular_inversa(matriz):
    determinante = calcular_determinante(matriz)
    
    # Considerar que el determinante es 0 si es menor que un umbral
    if abs(determinante) < 1e-6:
        raise ValueError("La matriz no tiene inversa, ya que el determinante es (casi) 0.")
    
    adjunta = calcular_adjunta(matriz)
    inversa = adjunta / determinante
    return inversa

def verificar_inversa(matriz, inversa):
    identidad = np.dot(matriz, inversa)
    identidad_redondeada = np.round(identidad, decimals=4)
    print("Confirmación de la matriz identidad:")
    print(identidad_redondeada)

    if np.allclose(identidad_redondeada, np.identity(matriz.shape[0])):
        print("La inversa es correcta.")
    else:
        print("La inversa no es correcta.")


# Principal

print("------------------------------------------------------------------")
matriz = obtener_matriz()

# Mostrar la matriz ingresada
print("------------------------------------------------------------------")
print("Matriz:")
print(np.round(matriz, decimals=4))  # Redondear la matriz para mostrarla con 4 decimales
print("------------------------------------------------------------------")

det = calcular_determinante(matriz)
print(f"Determinante: {round(det, 4)}")  # Redondear el determinante a 4 decimales
print("------------------------------------------------------------------")

# Si el determinante es cero o casi cero, se detiene el programa
if abs(det) < 1e-6:  # Umbral de 1e-6 para considerar cero
    print("La matriz es singular y no tiene inversa. El programa se detiene.")
else:
    traspuesta = calcular_traspuesta(matriz)
    print(f"Traspuesta:")
    print(np.round(traspuesta, decimals=4))  # Redondear la traspuesta
    print("------------------------------------------------------------------")

    adjunta = calcular_adjunta(matriz)
    print(f"Adjunta de la traspuesta (redondeada):")
    print(np.round(adjunta, decimals=4))  # Redondear la adjunta
    print("------------------------------------------------------------------")

    inversa = calcular_inversa(matriz)
    print(f"Inversa (redondeada):")
    print(np.round(inversa, decimals=4))  # Redondear la inversa
    print("------------------------------------------------------------------")

    verificar_inversa(matriz, inversa)
