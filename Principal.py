
from cliente import Cliente

infor_cliente = Cliente('César Freitas Costa', '29 anos', '426.131.228.03')

print('Cliente:')
print('nome:', infor_cliente.nome)
print('idade:', infor_cliente.idade)
print('cpf:', infor_cliente.cpf)
print()
conta_bancaria = Cliente(1500, 1000,1000,)

print('CONTA BANCÁRIA:')
print('Ag 0001 Conta 015253-8')
print('Total de Saldo:', conta_bancaria.nome)
print('limite Disponivel:', conta_bancaria.idade)
print()
saldo = input('apter enter para consultar o saldo:')
print(conta_bancaria.nome)

valor = int(input('DIGITE O VALOR DO SAQUE: '))
conta_bancaria.sacar(valor)
print('saque de', valor,'$',  '10/04')
print('Saldo -', conta_bancaria.nome)
print('Limite Diário -', conta_bancaria.idade)
print()
din = int(input('DIGITE O VALOR DO DEPÓSITO:'))
conta_bancaria.depositar(din)
print('Depósito de', din,'$', '11/09')
print('Total de Saldo', conta_bancaria.nome)
print('Limite Diário -', conta_bancaria.idade)

'''
infor_cliente2 = Cliente('Rafaela de Sá', '23 anos', '519.742.598.69')
print('Cliente:')
print('nome:', infor_cliente2.nome)
print('idade:', infor_cliente2.idade)
print('cpf:', infor_cliente2.cpf)
print()
conta_bancaria2 = Cliente(14100, 13000,14100,)

print('Conta Bancária:')
print('Ag 0001 Conta 015253-8')
print('Saldo total:', conta_bancaria2.nome)
print('limite Diário:', conta_bancaria2.idade)
print('Total de Saldo:', conta_bancaria2.cpf)

val = input('Digite o valor do saque: ')
print(val)
conta_bancaria2.sacar(valor)'''