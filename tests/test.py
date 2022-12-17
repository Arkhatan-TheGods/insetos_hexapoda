salario = float(input('digite o salário: '))
valor_emp = float(input('valor do empréstimo: '))
parcelas = int(input('quantidade de parcelas'))

def test_emprestimo(salario, valor_emp, parcelas):
    dezporcento = salario * 0.10
    totmes = valor_emp/parcelas
    if totmes < dezporcento:
        print('empréstimo aprovado.')  
    else:
        print('empréstimo negado.')
        
        
test_emprestimo(salario, valor_emp, parcelas)