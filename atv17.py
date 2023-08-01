def calcular_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps):
    velocidade_link_mbps = velocidade_link_mbps / 8  # Converter de Mbps para MBps
    tempo_segundos = tamanho_arquivo_mb / velocidade_link_mbps
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos

# Função principal
def main():
    try:
        tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
        velocidade_link_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

        tempo_download_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps)

        print(f"Tempo aproximado de download: {tempo_download_minutos:.2f} minutos")

    except ValueError:
        print("Erro: Valores inválidos. Certifique-se de digitar números válidos para o tamanho do arquivo e a velocidade do link.")

if __name__ == "__main__":
    main()
