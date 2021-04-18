# variaveis
azul = 0
vermelho = 0
amarelo = 0
voto_nulo = 0
voto_branco = 0

# quantidade de eleitores
eleitores = int(input("Qual o número de eleitores: "))

# loop
for n in range(eleitores):
    voto = int(input("vote em 1, 2, ou 3: "))
    if (voto == 1):
        azul = azul + 1
    elif (voto == 2):
        vermelho = vermelho + 1
    elif (voto == 3):
        amarelo = amarelo + 1
    elif (voto > 3):
        voto_nulo = voto_nulo + 1
    elif (voto == 0):
        voto_branco = voto_branco + 1
    else:
        print('Voto invalido')
        
# imprimir totais
total_votos = azul + vermelho + amarelo
print(f'{azul}')
print(f'{vermelho}')
print(f'{amarelo}')

# contagem de votos
total_az = float(azul / total_votos) * 100
total_ve = float(vermelho / total_votos) * 100
total_am = float(amarelo / total_votos) * 100
total_nu = float(voto_nulo / total_votos) * 100
total_br = float(voto_branco / total_votos) * 100

# saida de dados        
print(f'Total de votos Azul: {azul}, {total_az} %')
print(f'Total de votos Vermelho: {vermelho}, {total_ve} %')
print(f'Total de votos Amarelo: {amarelo}, {total_am} %')
print(f'Total de votos nulos: {voto_nulo}, {total_nu} %')
print(f'Total de votos brancos: {voto_branco}, {total_br} %')