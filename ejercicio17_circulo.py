"""Ejercicio Propuesto No 17"""

import math


class Circulo:

    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def calcular_circunferencia(self) -> float:
        return 2 * math.pi * self.radio

    def resultado(self):
        print(f"Área del círculo: {self.calcular_area():.2f}")
        print(f"Longitud de la circunferencia: {self.calcular_circunferencia():.2f}")


if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    circulo.resultado()
