import matplotlib.pyplot as plt


# First function used for the line graph
def line_graph(x, y, y_label, title):
    fig, ax = plt.subplots()  # We use subplots, so we can plot multiple charts at same time
    ax.grid()
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.plot(x, y, color='red', linewidth='3')


# Second function working fine
def tabla_2(total_sum, years, column_labels):
    fig, ax = plt.subplots()  # We use subplots, so we can plot multiple charts at same time
    columnheaders = column_labels  # Headers for the columns of the table
    list_years = years  # List of years
    total_per_year = total_sum  # List of total crimes per year
    l = [list_years, total_per_year]  # We store both list in one only list
    l = list(map(list, zip(*l)))  # We prepare the data so we can show it vertically
    ax.axis("off")
    ax.axis("tight")
    ax.table(cellText=l, loc='center', colLabels=columnheaders)


# Third function for pie chart
def grafica_pie(x, y):
    explode = (0, 0.1, 0, 0, 0)
    plt.pie(y, labels=x, autopct='%1.1f%%', explode=None,  shadow=True, startangle=180, counterclock=True)
    plt.show()
