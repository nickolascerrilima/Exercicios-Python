listanumerica = [2, 3, 6, 7, 10]

tamanho = 5 #vou colocar um input na lista numerica

while tamanho > 1: #tem que verificar se tem dois elementos para fazer a troca

    troca = False
    posicao = 0
    while posicao < tamanho - 1:
        if listanumerica[posicao] > listanumerica[posicao + 1]:
            
            troca = True
            temporaria = listanumerica[posicao]
            listanumerica[posicao] = listanumerica[posicao + 1]
            listanumerica[posicao + 1] = temporaria
        posicao += 1
        print(listanumerica)

    if not troca:#le dessa forma: se troca não, ou troca tem o valor não.
        break
    tamanho = tamanho - 1

#for x in listanumerica: #pra mostrar de forma unitária
    #print(x, end = ' ')

print(listanumerica)