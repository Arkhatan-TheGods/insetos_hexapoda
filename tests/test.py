
def test_emprestimo():
    salario = 5000
    valor_emp = 20000
    parcelas = 24
    dezporcento = salario * 0.10
    totmes = valor_emp/parcelas
    if totmes < dezporcento:
        print('empréstimo aprovado.')
    else:
        print('empréstimo negado.')
