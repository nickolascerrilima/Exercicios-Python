#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um numero inteiro: '))

resultado = numero % 2
#é porque 

if resultado == 1:
    print('Seu numero é impar')
else:
    print('Seu numero é par')
