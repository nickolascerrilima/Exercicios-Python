#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = input('Digite o nome da cidade: ').upper().split()
if "SANTO" in cidade[0]:
    print('Sua cidade começa com SANTO')
else:
    print('Sua cidade não começa com SANTO')