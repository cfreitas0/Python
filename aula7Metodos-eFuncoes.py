#FUNCAO DE SOMA
def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp
#variavel =
retorno = soma (12.45, 75.60)

print(retorno)

def tem_set_itens(argumento):
    if len (argumento) == 7:
        return True
    else:
        return False
#chamando a funçao de forma direta.
print(tem_set_itens('1234567'))

#usandoa funçao com if para retorno e printando na tela.
if tem_set_itens('cesarcr'):              #retorna true ou False
    print('realmente tem sete letras')