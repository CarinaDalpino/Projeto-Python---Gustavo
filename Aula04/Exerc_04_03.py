import csv

# Nome do arquivo CSV
arquivo = "Aula04/alunos.csv"

notas = []
aprovados = []
linhas_invalidas = 0

with open(arquivo, newline='', encoding="utf-8") as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # pula o cabeçalho

    for i, linha in enumerate(leitor, start=2):  # start=2 porque a linha 1 é o cabeçalho
        try:
            # Verifica se a linha tem exatamente 2 colunas
            if len(linha) != 2:
                raise ValueError("Número incorreto de colunas")

            nome, nota = linha
            nota = float(nota)  # pode dar erro se não for número
            notas.append(nota)

            if nota > 7:
                aprovados.append(nome)

        except Exception as e:
            print(f"⚠️ Linha {i} inválida: {linha} -> Erro: {e}")
            linhas_invalidas += 1

# Cálculo da média, só se houver notas válidas
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
    print("Alunos aprovados (nota > 7):")
    for aluno in aprovados:
        print(f"- {aluno}")
else:
    print("\nNenhuma nota válida encontrada.")

print(f"\nTotal de linhas inválidas: {linhas_invalidas}")
