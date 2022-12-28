import insetos_hexapoda.entities.pessoa as pe

def test_carrega_pessoa():
    pessoa = pe.Pessoa(250,'Rodrigo',30,'São Paulo')
    print(pessoa.id, pessoa.nome, pessoa.idade, pessoa.end)
    
def test_adicionar_pessoa():
    lista_pessoas = []
    for c in range(0,2):
        identify = int(input('id:'))
        nome = str(input('nome:'))
        idade = int(input('idade:'))
        end = str(input('endereço:'))
        pessoa = pe.Pessoa(identify, nome, idade, end)
        lista_pessoas.append(pessoa)
        print(lista_pessoas)