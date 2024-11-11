import numpy as np

def obtener_matriz():
    # Solicitar tamaño de la matriz
    while True:
        try:
            dimensiones = input("Introduce las dimensiones de la matriz en formato 'filas,columnas' (ejemplo: 3,3): ")
            filas, columnas = map(int, dimensiones.split(","))
            
            # Verificar si la matriz es cuadrada
            if filas != columnas:
                print("La matriz debe ser cuadrada. Vuelve a intentarlo.")
                continue
            break
        except ValueError:
            print("Formato inválido. Asegúrate de ingresar las dimensiones correctamente (ejemplo: 3,3).")

    matriz = []
    elementos_totales = filas * columnas
    elementos_ingresados = 0

    print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
    
    # Solicitar los elementos de la matriz
    while elementos_ingresados < elementos_totales:
        for i in range(filas):
            fila = input(f"Fila {i + 1} (ingresar {columnas} números separados por coma): ")
            try:
                fila_valores = list(map(float, fila.split(",")))
                if len(fila_valores) != columnas:
                    print(f"Error: Debes ingresar exactamente {columnas} valores.")
                    continue
                matriz.append(fila_valores)
                elementos_ingresados += len(fila_valores)
            except ValueError:
                print("Entrada no válida. Asegúrate de ingresar solo números separados por comas.")
    
    return np.array(matriz)

def calcular_determinante(matriz):
    return np.linalg.det(matriz)

def calcular_traspuesta(matriz):
    return np.transpose(matriz)

def calcular_adjunta(matriz):
    # Calcular la matriz de cofactores
    cofactores = []
    for i in range(matriz.shape[0]):
        fila_cofactores = []
        for j in range(matriz.shape[1]):
            submatriz = np.delete(np.delete(matriz, i, axis=0), j, axis=1)
            cofactor = ((-1) ** (i + j)) * np.linalg.det(submatriz)
            fila_cofactores.append(cofactor)
        cofactores.append(fila_cofactores)
    # Transponer la matriz de cofactores
    return np.transpose(cofactores)

def calcular_inversa(matriz):
    determinante = calcular_determinante(matriz)
    if determinante == 0:
        raise ValueError("La matriz no tiene inversa, ya que el determinante es 0.")
    adjunta = calcular_adjunta(matriz)
    inversa = adjunta / determinante
    return inversa

def verificar_inversa(matriz, inversa):
    # Multiplicar la matriz por su inversa
    identidad = np.dot(matriz, inversa)

    # Redondear el resultado para evitar números muy pequeños
    identidad_redondeada = np.round(identidad, decimals=4)

    print("Confirmación de la matriz identidad:")
    print(identidad_redondeada)

    # Verificar si el resultado es cercano a la matriz identidad
    if np.allclose(identidad_redondeada, np.identity(matriz.shape[0])):
        print("La inversa es correcta.")
    else:
        print("La inversa no es correcta.")

# Función principal
def main():
    print("------------------------------------------------------------------")
    
    # Obtener la matriz desde la terminal
    matriz = obtener_matriz()
    print("------------------------------------------------------------------")
    print(f"Matriz: \n {matriz}")
    print("------------------------------------------------------------------")
    
    # Calcular el determinante
    det = calcular_determinante(matriz)
    print(f"Determinante: {det}")
    print("------------------------------------------------------------------")

    # Calcular la traspuesta
    traspuesta = calcular_traspuesta(matriz)
    print(f"Traspuesta:\n{traspuesta}")
    print("------------------------------------------------------------------")

    # Calcular la adjunta
    adjunta = calcular_adjunta(matriz)
    # Redondear la adjunta para evitar decimales pequeños
    adjunta_redondeada = np.round(adjunta, decimals=4)
    print(f"Adjunta de la traspuesta (redondeada):\n(acuerdate del orden de los signos + y -)\n{adjunta_redondeada}")
    print("------------------------------------------------------------------")

    # Calcular la inversa
    try:
        inversa = calcular_inversa(matriz)
        # Redondear la inversa para evitar decimales muy pequeños
        inversa_redondeada = np.round(inversa, decimals=4)
        print(f"Inversa (redondeada):\n{inversa_redondeada}")
        print("------------------------------------------------------------------")
    except ValueError as e:
        print(e)
        return

    # Verificación de la inversa
    verificar_inversa(matriz, inversa_redondeada)

if __name__ == "__main__":
    main()  