import util
import graficas
import matplotlib.pyplot as plt


def init():
    data = util.readFile('\\IDEFC_NM_feb24.csv')
    util.cleanData(data)
    util.convertNumber(data)
    return data


def getDataAntesDeGraficar():
    flag = True

    while flag:
        data = init()  # First we initialize the data
        bienJuridico = util.getDistinct(data[1:], 3)  # Now we retrieve the all the posible options for 'Bien Juridico'

        opt = util.seleccionaDato(bienJuridico, 'Bien Jurídico')  # We display the menu options for 'Bien Juridico'
        if opt == -1:  # If the user chooses '-1' it means that he wants to exit and finish the code
            return 0, 0, 0  # The function stops and returns 'None'
        categoria = bienJuridico[opt]  # From all the possible categories, we select the one the user choose and save it

        matrizBienes = util.getFilterData(data[1:], 3, categoria)  # We create a new matrix filtered by the choosen option
        delitos = util.getDistinct(matrizBienes[1:], 4)  # Now we retrieve all the type of 'delitos' from the category

        optDelito = util.seleccionaDato(delitos, 'Tipo Delito')  # We display the new menu for the user to choose

        if optDelito == -1:  # If he choose '-1' we pass and then return to the first menu and change the category
            pass

        else:  # Else we move forward and graph all the data
            # We save the type of crime choosen by the user
            categoriaDelito = delitos[optDelito]
            # We create a new matrix filtered by the type of crime choosen
            matrizDelitos = util.getFilterData(data[1:], 4, categoriaDelito)

            # Ws sum all the incindences of each year and return a list of values
            suma_years = util.sumar_year(matrizDelitos)
            modalidad = util.getDistinct(matrizBienes[1:], 6)  # We retrieve all the type of 'modalidad'

            suma_modalidad, modalidad = util.sumar_modalidad(matrizDelitos, modalidad)

            return suma_years, suma_modalidad, modalidad


def main():
    while True:
        # We retrieve the total sum of years, total sum by 'modalidad' and each type of 'modalidad'
        data_filtered, data_modalidad, modalidad = getDataAntesDeGraficar()
        if data_filtered == 0:  # If the user chooses, he can finish the code execution
            print('Gracias, vuelva pronto')
            break
        years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]  # List of years for the graphs
        print(data_filtered)
        print(modalidad)
        print(data_modalidad)
        col_labels = ['Año', 'Total']

        graficas.line_graph(years, data_filtered, 'Delitos', 'Delitos cometidos por año')  # Recall for line graph
        graficas.tabla_2(data_filtered, years, col_labels)  # Recall for table of totals
        plt.show()  # Show both plots using 'subplots'

        graficas.grafica_pie(modalidad, data_modalidad)
        plt.show()  # Show both plots using 'subplots'


if __name__ == '__main__':
    main()
