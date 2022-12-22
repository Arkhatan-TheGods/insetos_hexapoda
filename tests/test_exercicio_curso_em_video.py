valores = (int(input('primeiro valor: ')), int(input('segundo valor: ')), int(input('terceiro valor: ')), int(input('quarto valor: ')))

par = 0

for valor in valores:
    if valor % 2 == 0:
        par += 1

print(f'você digitou os números: {valores}')

if 3 in valores:
    print(f'a primeira posição do número três ocorre: {valores.index(3)+1}ª posição.')
else:
    print('o valor 3 não foi digitado.')

    lista_times = setup

    times_sorted = sorted(lista_times)

    for i, pos in enumerate(times_sorted, 1):

        print(f"{i} - {pos}")

        time.sleep(.1)

def test_data():

    # endereco:str = "RUA PITON"
    endereco:int = 0

    assert type(endereco) == int

# print('-'*80)
# print('Posição do Chapecoense {}ª.'.format(times.index('Chapecoense ')+1))