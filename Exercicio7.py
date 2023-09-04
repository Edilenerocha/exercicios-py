salario = input("digite o salario do funcionario: ")
reajuste = input ("digite o percentual de reajuste: ")
novo_salario = float(salario)*(1+(float(reajuste)/100))

print(f"o novo salario e: {novo_salario}")