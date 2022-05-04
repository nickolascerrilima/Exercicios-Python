#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
primeiro_aluno = input('Nome do primeiro aluno: ')
segundo_aluno = input('Nome do segundo aluno: ')
terceiro_aluno = input('Nome do terceiro aluno: ')
quarto_aluno = input('Nome do quarto aluno: ')

lista_aluno = [terceiro_aluno, quarto_aluno, segundo_aluno, primeiro_aluno]

random.shuffle(lista_aluno)

print('A ordem será: {}'.format(lista_aluno))