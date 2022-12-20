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

if par > 0:
    print(f'total de números pares: {par}')
else:
    print('não foram digitados pares.')
if 9 in valores:
    print(f'o número nove apareceu: {valores.count(9)} vezes')
else:
    print('o número 9 não foi digitado.')