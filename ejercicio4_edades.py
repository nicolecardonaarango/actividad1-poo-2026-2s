"""Ejercicio Resuelto No 4"""

class EdadFamilia:
    def __init__(self, edad_juan: float):
        self.edad_juan = edad_juan
        self.edad_alberto = (2/3) * self.edad_juan
        self.edad_ana = (4/3) * self.edad_juan
        self.edad_mamajuan = self.edad_juan + self.edad_alberto + self.edad_ana

    def edades(self):
        print("** Las edades son: **")
        print(f"Juan: {self.edad_juan:.2f}")
        print(f"Alberto: {self.edad_alberto:.2f}")
        print(f"Ana: {self.edad_ana:.2f}")
        print(f"Mamá: {self.edad_mamajuan:.2f} ")

if __name__ == "__main__":
    edad_juan = float(input("Ingrese la edad de Juan: "))
    calcular = EdadFamilia(edad_juan)
    calcular.edades()