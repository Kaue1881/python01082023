import math

def calcular_quantidade_e_preco(area):
    # Cada litro de tinta cobre 6 metros quadrados, considerando 10% de folga
    litros_tinta = area / 6 * 1.1

    # Cálculo das latas de 18 litros
    latas_tinta_18 = math.ceil(litros_tinta / 18)
    preco_latas_18 = latas_tinta_18 * 80.00

    # Cálculo dos galões de 3,6 litros
    galoes_tinta_36 = math.ceil(litros_tinta / 3.6)
    preco_galoes_36 = galoes_tinta_36 * 25.00

    # Cálculo misturando latas e galões
    latas_tinta_mistura = math.floor(litros_tinta / 18)
    litros_restantes = litros_tinta % 18
    galoes_tinta_mistura = math.ceil(litros_restantes / 3.6)
    preco_mistura = (latas_tinta_mistura * 80.00) + (galoes_tinta_mistura * 25.00)

    return latas_tinta_18, preco_latas_18, galoes_tinta_36, preco_galoes_36, latas_tinta_mistura, galoes_tinta_mistura, preco_mistura

# Função principal
def main():
    try:
        tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

        if tamanho_area <= 0:
            print("Erro: O tamanho da área deve ser maior que zero.")
        else:
            latas_tinta_18, preco_latas_18, galoes_tinta_36, preco_galoes_36, latas_tinta_mistura, galoes_tinta_mistura, preco_mistura = calcular_quantidade_e_preco(tamanho_area)

            print(f"Comprando apenas latas de 18 litros:")
            print(f"Quantidade de latas: {latas_tinta_18}")
            print(f"Preço total: R$ {preco_latas_18:.2f}")

            print(f"\nComprando apenas galões de 3,6 litros:")
            print(f"Quantidade de galões: {galoes_tinta_36}")
            print(f"Preço total: R$ {preco_galoes_36:.2f}")

            print(f"\nMisturando latas e galões:")
            print(f"Quantidade de latas: {latas_tinta_mistura}")
            print(f"Quantidade de galões: {galoes_tinta_mistura}")
            print(f"Preço total: R$ {preco_mistura:.2f}")

    except ValueError:
        print("Erro: Valor inválido. Certifique-se de digitar um número válido para o tamanho da área.")

if __name__ == "__main__":
    main()
