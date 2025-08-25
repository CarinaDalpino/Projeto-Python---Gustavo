      
soma = 0 # inicializa a variável soma com 0, onde vamos acumular os valores
for numero in range(1, 101): # percorre os números de 1 até 100 (o range vai de 1 até 100, pois o final é exclusivo)
    if numero % 2 == 0: # verifica se o número é par (resto da divisão por 2 igual a 0)
        soma += numero # se for par, adiciona esse número à soma
print("Soma dos pares de 1 a 100:", soma) # ao final, exibe o resultado da soma de todos os pares de 1 a 100