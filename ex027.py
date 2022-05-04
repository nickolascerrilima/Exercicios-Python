#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite o seu nome completo: ').split()
print('O primeiro nome é {} e o ultimo nome é {} '.format(nome[0], nome[-1]))
#pode usar um len no lugar do -1 
