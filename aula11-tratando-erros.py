'''try:
    cgcwefb()
except ZeroDivisionError:
    print('Não pode ser feita essa divisao')  # indica erros matematicos

except NameError:
    print('Você digitou alguma coisa errada')  # indica erros de sitax nomes


try:
    open('')
except Exception as erro:
    print("Aconteceu algum erro", erro)   #indica qualquer tipo de erro'''

     # TENTANDO ABRIR UM PROGRAMA DE 5 EM 5S
import time
def abre_arquivo():
    try:
        arquivo = open('Sites-importantes')
        return True
    except Exception as erro:
        print('Aconteceu algum erro')
        return False

while not abre_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(6)

print('Consegui abrir o arquivo')

























