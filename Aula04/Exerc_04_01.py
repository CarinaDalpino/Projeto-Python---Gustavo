import csv

# Nome do arquivo CSV
arquivo = "Aula04/alunos.csv"

notas = []

# Lendo o CSV
with open(arquivo, newline='', encoding="utf-8") as csvfile:
    leitor = csv.DictReader(csvfile)
    
    print("Notas dos alunos:")
    for linha in leitor:
        nome = linha["nome"]
        nota = float(linha["nota"])
        notas.append(nota)
        print(f"{nome}: {nota}")

# Calculando a média
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
else:
    print("Nenhuma nota encontrada no arquivo.")

