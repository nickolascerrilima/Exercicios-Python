# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


frase = input('Digite uma frase: ').upper()
print('Existem {} A na frase'.format((frase.count('A'))))
print('A primeira vez que apareceu a letra A foi: {}'.format(frase.find('A')))
print('A ultima vez que apareceu a letra A foi: {}'.format(frase.rfind('A')))