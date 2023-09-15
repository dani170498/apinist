import wget
import gzip
import shutil
import os
import subprocess

# URL del archivo comprimido
url = "https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.gz"

# Nombre de archivo para el archivo comprimido descargado
archivo_comprimido = "/home/kali/apinist/archivos/official-cpe-dictionary_v2.3.xml.gz"

# Descargar el archivo comprimido
print("Descargando archivo comprimido...")
wget.download(url, archivo_comprimido)
print("\nDescarga completada.")

# Nombre de archivo para el archivo descomprimido
archivo_descomprimido = "/home/kali/apinist/archivos/official-cpe-dictionary_v2.3.xml"

# Descomprimir el archivo
print("Descomprimiendo archivo...")
with gzip.open(archivo_comprimido, 'rb') as f_in, open(archivo_descomprimido, 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)
print("Descompresión completada.")

# Eliminar el archivo comprimido si lo deseas
eliminar_archivo_comprimido = True
if eliminar_archivo_comprimido:
    os.remove(archivo_comprimido)
    print("Archivo comprimido eliminado.")

# Proceso de filtrado y redirección de la salida a un archivo
comando = (
    "cat /home/kali/apinist/archivos/official-cpe-dictionary_v2.3.xml | "
    "grep 'wordpress' | "
    "grep -v 'reference' | "
    "grep -v '<cpe-item name=\"' | "
    "grep -Eo 'name=.*' | "
    "grep -Eo '\".*\"' | "
    "sed 's/\"//g' >> /home/kali/apinist/archivos/cpe.txt"
)

print("Ejecutando proceso de filtrado y redirección...")
subprocess.run(comando, shell=True)
print("Proceso completado.")
os.remove(archivo_descomprimido)
print("Archivo XML eliminado.")

