horario = input('Em qual turno voce estuda ? digite "m" para matutino, "v" para vespertino e "n" para noturno : ').upper()

if horario == 'M':
    print(f'''Bom dia !
    Seja bem vindo ! ''')
elif horario == 'V':
    print(f'''Boa tarde !
    Seja bem vindo !''')
elif horario == 'N':
    print(f'''Boa noite !
          Seja bem vindo !''')

else:
    print(f'Turno Invalido, insira um TURNO valido')