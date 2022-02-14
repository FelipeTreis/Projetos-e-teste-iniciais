mb = float(input('insira o tamanho do arquivo que sera feito o download(Mb): '))
v = 30 #Mbps

velocidade_de_download = mb / v

print(f'o tempo de download sera de {round(velocidade_de_download, )} minutos.')