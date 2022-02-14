class Quadrado:
    def __init__(self, lado = 1):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

quadrado = Quadrado(float(input('Qual o lado do quadrado: ')))
print(f'''o lado do quadrado e igua a: {quadrado.lado} 
e a area do quadrado e igua a: {quadrado.calcular_area()}''')
