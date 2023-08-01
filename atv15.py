import math

def calcular_latas_e_preco(area):
    # Cada litro de tinta cobre 3 metros quadrados
    litros_tinta = area / 3

    # Cada lata de tinta tem 18 litros
    latas_tinta = math.ceil(litros_tinta / 18)

    # Cálculo do preço total
    preco_lata = 80.00
    preco_total = latas_tinta * preco_lata

    return latas_tinta, preco_total

# Função principal
def main():
    try:
        tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
        
        if tamanho_area <= 0:
            print("Erro: O tamanho da área deve ser maior que zero.")
        else:
            latas_tinta, preco_total = calcular_latas_e_preco(tamanho_area)

            print(f"Quantidade de latas de tinta a serem compradas: {latas_tinta}")
            print(f"Preço total: R$ {preco_total:.2f}")

    except ValueError:
        print("Erro: Valor inválido. Certifique-se de digitar um número válido para o tamanho da área.")

if __name__ == "__main__":
    main()
