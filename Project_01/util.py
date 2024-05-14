import os


def readFile(fileName):

    data = []
    path = os.path.dirname(__file__)
    # csvFile = 'IDEFC_NM_feb24.csv'
    encoding = 'Windows 1252'
    with open(path + fileName, 'r', encoding=encoding) as f:
        for line in f:
            line = line.replace('cables, tubos', 'cables tubos')
            newLine = line.split(',')
            data.append(newLine)
    return data


def getNumber(x):
    if x.isnumeric():
        return int(x)
    else:
        return x


def convertNumber(data):
    for i in range(len(data)):
        data[i] = list(map(getNumber, data[i]))  # aplicar una funcion a todos los element de una lista usando MAP


def cleanData(data):
    for linea in data:
        linea[-1] = linea[-1][:-1] if '\n' in linea[-1] else linea[-1]


def getDistinct(data, column):  # opciones del encabezado 'bien juridico afectado'
    nuevaLista = []
    for line in data: 
        # for col in line[3:4]:  
        for col in line[column:column + 1]:   
            if col not in nuevaLista:
                nuevaLista.append(col)

    return nuevaLista


def seleccionaDato(opcionesJuridico, string):
    n = 0
    print('*' * 80)
    # print('**{:<90}**'.format(string))
    print(string.center(80,'*'))
    print('*' * 80)
    for opciones in opcionesJuridico:
        print(f'{"**":4}({n}).- {opciones}')
        n += 1 
    print(f'{"**":4}{"(-1)"}.- Salir')
    print('*' * 80)
    opt = int(input('** Seleccione una opcion ==> '))
    return opt


def getFilterData(data, column, categoria):
    listaFiltrada = []
    for line in data:
        if line[column] == categoria:
            listaFiltrada.append(line) 
    return listaFiltrada


# Function used to sum the total for each year of the CSV document
def sumar_year(data):

    suma2015 = 0
    suma2016 = 0
    suma2017 = 0
    suma2018 = 0
    suma2019 = 0
    suma2020 = 0
    suma2021 = 0
    suma2022 = 0
    suma2023 = 0
    suma2024 = 0
    for line in data:
        if line[0] == 2015:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2015 += valor
                else:
                    suma2015 += valor
        elif line[0] == 2016:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2016 += valor
                else:
                    suma2016 += valor
        elif line[0] == 2017:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2017 += valor
                else:
                    suma2017 += valor
        elif line[0] == 2018:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2018 += valor
                else:
                    suma2018 += valor
        elif line[0] == 2019:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2019 += valor
                else:
                    suma2019 += valor
        elif line[0] == 2020:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2020 += valor
                else:
                    suma2020 += valor
        elif line[0] == 2021:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2021 += valor
                else:
                    suma2021 += valor
        elif line[0] == 2022:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2022 += valor
                else:
                    suma2022 += valor
        elif line[0] == 2023:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2023 += valor
                else:
                    suma2023 += valor
        elif line[0] == 2024:
            for valor in line[7:]:
                if valor == '':
                    valor = 0
                    suma2024 += valor
                else:
                    suma2024 += valor
    suma2 = [suma2015, suma2016, suma2017, suma2018, suma2019, suma2020, suma2021, suma2022, suma2023, suma2024]
    return suma2


# Function used to sum the total for each 'modalidad' of the CSV document
def sumar_modalidad(data, modalidad):
    data = data
    modalidad = modalidad
    suma = 0
    sumas_totales = []

    # First we sum the total by each 'modalidad'
    for modo in modalidad:  # ['arma  blanca', 'arma de fuego', 'aborto', 'transito']
        for line in data:
            if line[6] == modo:
                for valor in line[7:]:
                    if valor == '':
                        valor = 0
                        suma += valor
                    else:
                        suma += valor
        sumas_totales.append(suma)
        suma = 0

    # Now, we check if any index of the total sum is 0, and in case it is, we take it from the list because is None
    flag = True  # Flag used to repeat the process until no zero remains
    while flag:
        for indice, total in enumerate(sumas_totales):  # We save the item and its index
            if total == 0:
                sumas_totales.pop(indice)  # If the item is 0 we pop it out from the list
                modalidad.pop(indice)  # Here too

        # Once a list has used the 'pop' method it returns the lists and break the 'for', but due to the flag it will
        # repeeat the process again and again
        if 0 in sumas_totales:  # If any 0 number remains in the list, the flag remains true and process is repeated
            flag = True
        else:  # If no 0 remains in the list, the list is ready, and we can stop the searching process
            flag = False

    return sumas_totales, modalidad  # We return the 2 final lists


def main():
    pass


if __name__ == '__main__':
    main()
