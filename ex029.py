#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite um valor para a velocidade do seu carro: '))

multa = 7 * (velocidade - 80)

if velocidade > 80:
    print(f'Você foi multado :( sua multa é {multa} ')
else:
    print('Voce dirige muito bem!!')