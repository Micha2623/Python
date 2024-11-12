import matplotlib.pyplot as plt
import numpy as np

# Genera datos aleatorios (por ejemplo, una distribución normal)
data = np.random.randn(1000)

# Crea el histograma
plt.hist(data, bins=30, color='yellow', edgecolor='black')

# Añade títulos y etiquetas
plt.title("Histograma de datos aleatorios")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")

# Muestra el gráfico
plt.show()
