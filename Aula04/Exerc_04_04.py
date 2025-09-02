import csv
import logging

# Configuração do log para console + arquivo
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Formato do log
formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Log no arquivo
arquivo_handler = logging.FileHandler("processamento.log", encoding="utf-8")
arquivo_handler.setFormatter(formato)
logger.addHandler(arquivo_handler)

# Log no console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formato)
logger.addHandler(console_handler)

# Nome do arquivo CSV
arquivo = "alunos.csv"

notas = []
aprovados = []
linhas_invalidas = 0

try:
    logging.info("Início do processamento do arquivo CSV.")

    with open(arquivo, newline='', encoding="utf-8") as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)  # pula o cabeçalho

        for i, linha in enumerate(leitor, start=2):  # start=2 porque a linha 1 é cabeçalho
            try:
                if len(linha) != 2:
                    raise ValueError("Número incorreto de colunas")

                nome, nota = linha
                nota = float(nota)
                notas.append(nota)

                if nota > 7:
                    aprovados.append(nome)

            except Exception as e:
                logging.warning(f"Linha {i} inválida: {linha} -> Erro: {e}")
                linhas_invalidas += 1

    # Cálculo da média
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
        print("Alunos aprovados (nota > 7):")
        for aluno in aprovados:
            print(f"- {aluno}")
    else:
        print("\nNenhuma nota válida encontrada.")

    print(f"\nTotal de linhas inválidas: {linhas_invalidas}")
    logging.info("Fim do processamento do arquivo CSV.")

except FileNotFoundError as e:
    logging.error(f"Arquivo não encontrado: {arquivo} -> {e}")
    print("❌ Erro: Arquivo não encontrado.")
except Exception as e:
    logging.error(f"Erro inesperado ao processar o arquivo {arquivo} -> {e}")
    print("❌ Erro inesperado durante o processamento.")
