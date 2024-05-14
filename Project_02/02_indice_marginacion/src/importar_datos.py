import os.path
from pathlib import Path
import csv
import configuracion  # We import 'configuracion' since we have there the files routes
from manejador_sqlite.tablas_sqlite import TablaSQLite  # We import the class 'TablaSQLite' with all their methods


def cargar_csv(ruta_csv: str | Path):
    """
    Carga un archivo CSV, pero retorna cada fila en forma de diccionario que mapea el nombre de la columna al valor
    correspondiente. Todos los valores son retornados como texto. Los nombres de las columnas corresponden a como están
    definidas en el archivo CSV.
    """
    # Cargamos las filas en una lista para insertarlas después
    with open(ruta_csv, 'r') as archivo:  # We open the csv in reading mode by passing the file route
        reader = csv.DictReader(archivo)  # This method creates a dictionary using the CSV file
        return list(reader)


# PROYECTO - listo
def importar_csv(ruta_csv: str | Path, tabla: TablaSQLite, forzar: bool = False):
    """
    Recibe la ruta de una tabla CSV `ruta_csv`, también una instancia de una tabla que hereda de
    `manejador_sqlite.tablas_sqlite.TablaSQLite`, si quieren pueden asumir que es una instancia de la tabla
    `TablaMarginacion`,solo asegúrense de que el arhivo sqlite usado para la tabla sea el que está definido
    `configuracion.RUTA_BD`. Como la tabla ya es una instancia entonces pueden utilizar directamente el método
    `tabla.insert`.

    * La función debe de leer las filas del arhivo csv especificado en `ruta_csv` y meterlas en la tabla especificada
    en `tabla`.
    Pistas: No olviden utilizar la función anterior que ya está imlementada `cargar_csv`. Al usar el método insert
    aunque los valores vayan todos como `str` SQLite los convierte automáticamente al tipo de dato asociado a la
    columna, por lo que no hay que preocuparse por convertirlos.

    * Los datos se deben de importar únicamente si no se han importado anteriormente, para garantizar esto una vez
    importados los datos se debe de crear un archivo en la carpeta especificada por `configuracion.RUTA_DATOS_PROGRAMA`,
    con el nombre que quieran aunque sea vacío, el hecho de que exista significará que los datos ya fueron importados.
    Como consecuencia de esto, antes de comenzar a importar los datos debemos revisar si este archivo existe, si ya
    existe entonces la función debe mostrar el mensaje `"Datos ya importados, no se importarán. Usar 'forzar=True' para
    forzar la importación"` y retornar de la función.
    
    * Si el parámetro `forzar` es `True`, entonces los datos se deben importar siempre aunque el archivo indicador
    exista, eliminando el contenido de la tabla SQLite antes de comenzar la importación. Pistas: utilizar el
    método `tabla.delete`.
    """
    # If the text file doesn't exist, the database will be imported, this is the first level of jerarchy
    if not (os.path.isfile(configuracion.RUTA_DATOS_PROGRAMA/'DataBaseCreada.txt')):
        print('Importando información a la base de datos')
        lista_datos = cargar_csv(ruta_csv)  # We transform the csv data into a dict using 'cargar_csv()'
        tabla.insert(lista_datos)  # We insert the resulting list into the SQL DataBase
        with open(configuracion.RUTA_DATOS_PROGRAMA/'DataBaseCreada.txt', 'a') as archivo:
            archivo.write('Base de datos creada')  # Finally we create a text file meaning that the data was imported

    # If the data has been imported, and forzar is false, we will not import the data again
    elif os.path.isfile(configuracion.RUTA_DATOS_PROGRAMA/'DataBaseCreada.txt') and forzar is False:
        print("Datos ya importados, no se importarán. Usar 'forzar=True' para forzar la importación")

    # If user chooses 'forzar' and 'DataBaseCreada.txt' already exist, we will delete the data first and then import
    elif forzar:
        print('Base de datos eliminada, volviendo a importar información')
        tabla.delete()
        lista_datos = cargar_csv(ruta_csv)
        tabla.insert(lista_datos)

    if not (os.path.isfile(configuracion.RUTA_DATOS_PROGRAMA / 'Existe.txt')):
        lista_datos = cargar_csv(ruta_csv)
        tabla.insert(lista_datos)
        with open(configuracion.RUTA_DATOS_PROGRAMA / 'Existe.txt', 'a') as archivo:
            archivo.write('Existe')
