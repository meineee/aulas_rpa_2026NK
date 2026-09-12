import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    handlers=[
        logging.FileHandler('execucao_bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def processar_arquivo(caminho: str):
    logging.info(f"Iniciando o processamento do arquivo: {caminho}")
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            for i, linha in enumerate(arquivo, start=1):
                conteudo = linha.strip()
                logging.info(f"Linha {i} lida: {conteudo}")
    except FileNotFoundError:
        logging.error(f"Erro: O arquivo '{caminho}' não foi encontrado.")
    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado ao ler o arquivo '{caminho}': {e}")
    finally:
        logging.info(f"Tentativa de processamento do arquivo '{caminho}' finalizada.")

if __name__ == "__main__":
    processar_arquivo("arquivo_teste.csv")