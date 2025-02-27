quinze = 0
trinta = 0
quarenta = 0
sessenta = 0
maior = 0

for i in range(15):
    num = int(input(f"Idade da pessoa {i+1}: "))
    if num <= 15:
        quinze += 1
    elif num <= 30:
        trinta += 1
    elif num <= 45:
        quarenta += 1
    elif num <= 60:
        sessenta += 1
    else:
        maior += 1

print(f"""
Até 15 anos = {quinze} | {(quinze / 15) * 100:.2f}%
De 16 a 30 anos = {trinta} | {(trinta / 15) * 100:.2f}%
De 31 a 45 anos = {quarenta} | {(quarenta / 15) * 100:.2f}%
De 46 a 60 anos = {sessenta} | {(sessenta / 15) * 100:.2f}%
Acima de 61 anos = {maior} | {(maior / 15) * 100:.2f}%
""")
