import insetos_hexapoda.entities.pessoa as pe

def test_carrega_pessoa():
    pessoa = pe.Pessoa(250,'Rodrigo',30,'São Paulo')
    print(pessoa.id, pessoa.nome, pessoa.idade, pessoa.end)
    