#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
nome_sem_espaco =  len(nome) - (nome.count(' '))
primeiro_nome = nome.split()
print('Seu nome completo em caps é {} '.format(nome.upper()))
print('Seu nome completo normal é {} '.format(nome.lower()))
print('Seu nome tem {} caracteres sem espaço'.format(nome_sem_espaco))
print('Seu primeiro nome tem {} letras'.format(len(primeiro_nome[0])))
