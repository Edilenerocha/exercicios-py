print("informe sua idade em anos, meses e dias")

anos = input("digite quantos anos: ")
meses = input("digite quantos meses: ")
dias = input("digite quantos dias: ")

total_dias = int(dias) + (365 * int(anos)) + (30 * int(meses))

print(f"sua idade em dias e:{total_dias} ")