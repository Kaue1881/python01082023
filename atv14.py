## Descontos --
IR = float(11/100) 
INSS = float(8/100) 
Sindicato = int(5/100)

## Horas Trabalhadas e Ganhos --

HorasTrabalhadas = float(input("horas trabalhadas no mês: "))
GanhoPHora = float(input("Ganho por Hora: "))

## Salário --

salario = HorasTrabalhadas * GanhoPHora
salarioLiquido = salario - (IR*salario) - (INSS*salario) - (Sindicato*salario)

print ("Seu salario é: ", salarioLiquido)