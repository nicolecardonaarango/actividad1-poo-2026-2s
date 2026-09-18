"""Ejercicio Propuesto No 14"""

class Numero:

    def __init__(self, valor: float):
        self.valor = valor

    def calcular_cuadrado(self) -> float:
        return self.valor ** 2

    def calcular_cubo(self) -> float:
        return self.valor ** 3

    def calcular(self):
        print(f"El cuadrado de {self.valor} es {self.calcular_cuadrado():.2f}")
        print(f"El cubo de {self.valor} es {self.calcular_cubo():.2f}")


if __name__ == "__main__":
    valor = float(input("Ingrese un número: "))
    numero = Numero(valor)
    numero.calcular()
