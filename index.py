import csv
import os

# Nombre del archivo de texto de entrada
input_file = '..datos/MX.txt'  # Cambia esto por el nombre de tu archivo de texto
# Nombre del archivo CSV de salida
output_file = '..datos/MX.csv' # Cambia esto por el nombre de tu archivo de texto

try:
    # Verificar si la carpeta de salida existe
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Lee el archivo de texto y escribe en un archivo CSV
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter='\t')  # Asumiendo que los datos están separados por tabulaciones
        writer = csv.writer(outfile)
        
        # Escribir la cabecera (opcional)
        writer.writerow(['Código Estado', 'Código Localidad', 'Nombre Localidad', 'Municipio', 
                         'Código Municipio', 'Estado', 'Código Estado', 'Nombre Estado', 
                         'Código adicional', 'Latitud', 'Longitud', 'Número adicional'])

        # Escribir las filas
        for row in reader:
            writer.writerow(row)

    print(f"Los datos se han convertido y guardado en {output_file}.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo de entrada {input_file}.")
except Exception as e:
    print(f"Se produjo un error: {e}")