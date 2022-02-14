class CirculoPerfeito:
    def __init__(self):
        self.cor = input('insira uma cor para o circulo: ')
        self.circunferencia = float((input('insira uma circunferencia para o circulo: ')))
        self.material = input('insira um material para o circulo: ')

circulo_primeiro = CirculoPerfeito()

print(f'a cor do circulo e: {circulo_primeiro.cor}')
print(f'a circunferencia do circulo e: {circulo_primeiro.circunferencia}')
print(f'o material do circulo e: {circulo_primeiro.material}')
