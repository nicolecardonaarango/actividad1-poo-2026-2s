"""Ejercicio Propuesto No 12"""

class Salario:
    def __init__ (self, horas_trabajadas: float, valor_hora: float, porcentaje_retencion: float = 12.5):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion 

    def calcular_salario_bruto(self) -> float:
        return self.horas_trabajadas * self.valor_hora

    def calcular_retencion_fuente(self) -> float:
        return self.calcular_salario_bruto() * (self.porcentaje_retencion / 100)

    def calcular_salario_neto(self) -> float:
        return self.calcular_salario_bruto() - self.calcular_retencion_fuente()

    def resultado(self):
        print("La liquidación es: ")
        print(f"Salario bruto: ${self.calcular_salario_bruto():.2f}")
        print(f"Retencion en la fuente ({self.porcentaje_retencion}%): ${self.calcular_retencion_fuente():.2f}")
        print(f"Salario neto: ${self.calcular_salario_neto():.2f}")

if __name__ == "__main__":
    horas_trabajador = float(input("Ingrese las horas trabajadas: "))
    valor_hora = float(input("Ingrese el valor de la hora: "))
    salario = Salario(horas_trabajador, valor_hora)
    salario.resultado()
