import csv

# Nome do arquivo CSV
arquivo = "Aula04/alunos.csv"

notas = []
aprovados = []

with open(arquivo, newline='', encoding="utf-8") as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # pula o cabeçalho

    for linha in leitor:
        nome, nota = linha
        nota = float(nota)
        notas.append(nota)

        if nota > 7:
            aprovados.append(nome)

# Cálculo da média
media = sum(notas) / len(notas)

print(f"Média da turma: {media:.2f}")
print("Alunos aprovados (nota > 7):")
for aluno in aprovados:
    print(f"- {aluno}")