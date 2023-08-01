## a informação deve ser passada com um (.) e nã uma virgula, ex: (1.87)
altura = float(input("Altura: "))

## para informações de sexo, digite 1 para homem e 2 para mulher
sexo = float(input("Sexo: "))
kgHomens = (72.7*altura) - 58
KgMulher = (62.1*altura) - 44.7

if sexo == 1:
    print ("Seu peso é: ", kgHomens, "kg e você se identifica como homem")
elif sexo == 2:
    print ("Seu peso é: ", KgMulher, "kg e você se identifica como mulher")