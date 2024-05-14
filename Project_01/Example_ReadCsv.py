import os


def read_csv():
    tabla = []
    path = os.path.dirname(__file__)
    print(path)
    with open(path + '\\datos.csv', 'r', encoding='UTF-8') as f:
        for line in f:
            renglon = line.split(",")
            tabla.append(renglon)
    return tabla


def get_number(x):
    if '.' in x:
        return float(x)
    elif x.isnumeric():
        return int(x)
    else:
        return x


def convert_number(m):
    for i in range(len(m)):
        m[i] = list(map(get_number, m[i]))


def clean_data(m):
    for linea in m:
        linea[-1] = linea[-1][:-1] if '\n' in linea[-1] else linea[-1]


def print_matric(m):
    for line in m:
        for col in line:
            print(f'{col}'.rjust(12), end='')
        print()  # Enter


def main():
    # Matrix or object array
    matriz = read_csv()
    # Since our matrix is an object, we don't need to return anything, because we are modifying the object
    clean_data(matriz)
    convert_number(matriz)
    print_matric(matriz)
    print(matriz)


if __name__ == '__main__':
    main()
