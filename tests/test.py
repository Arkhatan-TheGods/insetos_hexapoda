
def emprestimo(salario: float, valor_emp: float, parcelas: int) -> bool:

    dezporcento = salario * 0.10
    total_mes = valor_emp/parcelas

    status_emprestimo = False

    if total_mes < dezporcento:
        status_emprestimo = True

    return status_emprestimo


def test_pass_emprestimo():

    salario = 5000
    valor_emp = 4000
    parcelas = 24

    assert emprestimo(salario, valor_emp, parcelas) == True


def test_failed_emprestimo():

    salario = 5000
    valor_emp = 20000
    parcelas = 24

    assert emprestimo(salario, valor_emp, parcelas) == False
