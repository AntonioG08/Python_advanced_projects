# Implementa tu solución aquí
import math
from plano_cartesiano import PlanoCartesiano
from plano_cartesiano import Color
from punto_cartesiano import PuntoCartesiano


class GraficaFuncion(PlanoCartesiano):
    def __init__(self, funcion, dx=0.1):
        super().__init__(Color.BLANCO, 1000, 800, (-20, 20), (-20, 20))

        # Guardamos la función en un atributo
        self._f = funcion
        # Guardamos también la separación entre cada evaluación de la función
        self.dx = dx
        # Atributo donde será generada la gráfica
        self._grafica = None
    
    def _construir_grafica(self):
        r"""
        Esta función debe generar una lista de objetos `PuntoCartesiano`.
        La lista no se debe retornar, sino que debe quedar almacenada en 
        el atributo privado `self._grafica`.

        Implementarla de acuerdo a las instrucciones dadas en el archivo
        `README.md`.
        """
        self._grafica = []
        x = self.x_dominio[0]
        while x <= self.x_dominio[1]:
            punto = PuntoCartesiano(x, self._f(x))
            self._grafica.append(punto)
            x += self.dx

        punto = PuntoCartesiano(self.x_dominio[1], self._f(self.x_dominio[1]))
        self._grafica.append(punto)
    
    def dibujar_escena(self):
        r"""
        Esta función debe dibujar lineas entre cada pareja de puntos consecutivos
        de la lista `self._grafica`, usando el método `self.linea_cart(...)`.

        Implementarla de acuerdo a las instrucciones dadas en el archivo
        `README.md`.
        """
        self._construir_grafica()
        for i in range(len(self._grafica) - 1):
            self.linea_cart(self._grafica[i], self._grafica[i + 1], Color.NEGRO)
#


def x_cuadrada(x):
    return x*x


if __name__ == "__main__":
    grafica = GraficaFuncion(x_cuadrada)
    # IMPORTANTE: si por alguna razón requieren que no se inicie el ciclo 
    # de dibujado en la ventana, comenten la siguiente linea.
    grafica.iniciar()
