def soma(a, b):

    CONST_SOMA = 10

    resultado = (a + b) + CONST_SOMA

    return resultado
   
def test_soma():

    a = int("2")
    
    b = int("2")

    print()

    print("a:",type(a))
    
    print("b:",type(b))

    resposta = soma(a,b)

    print("resposta>>>>>>", resposta)

    assert resposta == 4