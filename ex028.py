#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

numero_usuario = int(input('DIgite um valor de 0 a 5 e tente adivinhar o certo: '))
numero_robo = random.randint(0,5)#no randint o range funciona ja com o +1

print('PROCESSANDO')
sleep(1.5)

if numero_usuario == numero_robo:
    print('Parabens!!! você é um adivinho')
else:
    print('É uma pena, mas não conseguisse')
