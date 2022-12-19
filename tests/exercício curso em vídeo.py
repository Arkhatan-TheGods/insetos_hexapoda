times = ('Corinthians ','Palmeiras ','Santos ','Grêmio ','Cruzeiro ',
         'Flamengo ','Vasco da Gama ','Chapecoense ','Atlético-MG ',
         'Botafogo ','Athletico-PR ','Bahia ','São Paulo ','Fluminense',
         'Sport Recife ','EC Vitória ','Coritiba ','Avaí ','Ponte Preta ',
         'Atlético-GO ')
print('Os cinco primeiros:', end= ' ')
for cont in range(0,5):
    print(f' {times[cont]}', end=' ')
print('-'*80)
print('Os quatro últimos:', end='')
for cont in range(-1,4):
    print(f' {times[cont]}', end= '')
print('-'*80)
print(f' \n Ordem alfabética {sorted(times)}.')
print(f'\nOrdem alfabética:', end=' ')
for pos in times:
    sorted(times)
    print(pos, end=' ')
print('-'*80)
print('Posição do Chapecoense {}ª.'.format(times.index('Chapecoense ')+1))