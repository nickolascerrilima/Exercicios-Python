#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite um numero de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('O numero {} está na casa das unidade milhar'.format(milhar))
print('O numero {} está na casa das centenas'.format(centena))
print('o numero {} está na casa dos decimais'.format(dezena))
print('o numero {} está na casa das unidades'.format(unidade))