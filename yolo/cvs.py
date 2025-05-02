import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Cargar el archivo CSV
csv_file = r'C:\Users\micha\Downloads\pdcsvdetexport.csv'  # Asegúrate de que la extensión sea .csv
data = pd.read_csv(csv_file)

# Crear un PDF
pdf_file = 'archivo_convertido.pdf'  # Nombre del archivo PDF de salida
with PdfPages(pdf_file) as pdf:
    for i in range(0, len(data), 20):  # Dividir los datos en páginas (20 filas por página)
        plt.figure(figsize=(12, 8))
        plt.axis('off')
        
        # Crear una tabla en el PDF
        table = plt.table(cellText=data.iloc[i:i+20].values, colLabels=data.columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.2)  # Ajustar el tamaño de la tabla
        
        # Estilo para los encabezados
        for (i, j), cell in table.get_celld().items():
            if i == 0:  # Encabezados
                cell.set_text_props(fontweight='bold', color='white')
                cell.set_facecolor('blue')
            else:
                cell.set_facecolor('lightgrey' if i % 2 == 0 else 'white')  # Alternar colores
        
        plt.title('Datos del CSV', fontsize=16)
        pdf.savefig()  # Guardar la figura en el PDF
        plt.close()