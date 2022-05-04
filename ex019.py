#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

primeiro_aluno = input('Nome do primeiro aluno: ')
segundo_aluno = input('Nome do segundo aluno: ')
terceiro_aluno = input('Nome do terceiro aluno: ')
quarto_aluno = input('Nome do quarto aluno: ')

lista_aluno = [terceiro_aluno, quarto_aluno, segundo_aluno, primeiro_aluno]
escolhido = choice(lista_aluno)

print('O aluno escolhido foi o(a): {}'.format(escolhido))