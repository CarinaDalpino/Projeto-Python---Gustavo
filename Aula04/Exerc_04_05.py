import csv
import logging

# Configuração do log para console + arquivo
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

arquivo_handler = logging.FileHandler("processamento.log", encoding="utf-8")
arquivo_handler.setFormatter(formato)
logger.addHandler(arquivo_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formato)
logger.addHandler(console_handler)

# Nome dos arquivos
arquivo_entrada = "Aula04/alunos.csv"
arquivo_saida = "resultado.csv"

notas = []
linhas_invalidas = 0
resultados = []  # lista para salvar os dados de saída

try:
    logging.info("Início do processamento do arquivo CSV.")

    with open(arquivo_entrada, newline='', encoding="utf-8") as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)  # pula o cabeçalho

        for i, linha in enumerate(leitor, start=2):
            try:
                if len(linha) != 2:
                    raise ValueError("Número incorreto de colunas")

                nome, nota = linha
                nota = float(nota)
                notas.append(nota)

                situacao = "Aprovado" if nota > 7 else "Reprovado"
                resultados.append([nome, nota, situacao])

            except Exception as e:
                logging.warning(f"Linha {i} inválida: {linha} -> Erro: {e}")
                linhas_invalidas += 1

    # Cálculo da média
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida encontrada.")

    print(f"\nTotal de linhas inválidas: {linhas_invalidas}")

    # Gerar novo CSV com resultados
    with open(arquivo_saida, "w", newline="", encoding="utf-8") as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(["Nome", "Nota", "Situação"])
        escritor.writerows(resultados)

    logging.info(f"Arquivo '{arquivo_saida}' gerado com sucesso.")
    logging.info("Fim do processamento do arquivo CSV.")

except FileNotFoundError as e:
    logging.error(f"Arquivo não encontrado: {arquivo_entrada} -> {e}")
    print("❌ Erro: Arquivo não encontrado.")
except Exception as e:
    logging.error(f"Erro inesperado ao processar o arquivo {arquivo_entrada} -> {e}")
    print("❌ Erro inesperado durante o processamento.")
