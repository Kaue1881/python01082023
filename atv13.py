Multa = 4
LimiteDePeso = 50
peso = float(input("O peso de peixes trago hoje é: "))
## as informações devem ser colocadas apenas em números, ex: 56, 43, 80

if peso >= 50:
    pesoRestante = peso - 50
    conta = Multa * pesoRestante
    print ("Sua multa é de ", conta, " reais")
else:
    print ("Você não Pagara multa")