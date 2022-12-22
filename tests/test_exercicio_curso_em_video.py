import time
import pytest

# print('Os cinco primeiros:', end= ' ')

# for cont in range(0,5):
#     print(f' {times[cont]}', end=' ')

# print('-'*80)
# print('Os quatro últimos:', end='')

# for cont in range(-1,4):
#     print(f' {times[cont]}', end= '')

# print('-'*80)
# print(f' \n Ordem alfabética {sorted(times)}.')
# print(f'\nOrdem alfabética:', end=' ')

@pytest.fixture(scope='module')
def setup():
    
    times = ('Corinthians ','Palmeiras ','Santos ','Grêmio ','Cruzeiro ',
            'Flamengo ','Vasco da Gama ','Chapecoense ','Atlético-MG ',
            'Botafogo ','Athletico-PR ','Bahia ','São Paulo ','Fluminense',
            'Sport Recife ','EC Vitória ','Coritiba ','Avaí ','Ponte Preta ',
            'Atlético-GO ')

    return times

def test_ordena_times(setup):

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