for i in range(3): 
    idade = int(input("Digite sua idade: "))
    
    if idade < 12:
        print("Criança")
    elif idade < 18:
        print("Adolescente")
    else:
        print("Adulto")