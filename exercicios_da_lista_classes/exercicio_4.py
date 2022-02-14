class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def engordar(self):
        if self.idade < 21:
            self.peso += 1
        self.idade += 1


felipe = Pessoa('Felipe', 5, 60, 170)

for _ in range(40):
    felipe.envelhecer()
    print(f'idade de {felipe.nome} e: {felipe.idade} anos. e sua altura e {felipe.altura} cm. e seu peso e {felipe.peso} kg.')
