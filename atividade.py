def calcular_media(notas):
    total = 0
    
    for nota in notas:
        total += nota
    media = total / len(notas)
    return media


notas = []
continuar = 's'

while continuar.lower() == 's':
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    continuar = input("Deseja digitar outra nota? (s/n): ")

media_final = calcular_media(notas)

print(f"\nMédia final do aluno: {media_final:.2f}")

if media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")
   