carros_vendidos = int(input("digite o total de carros vendidos: "))
total_vendas = float(input("digite o total de vendas: "))
salario_fixo = float(input("digite o salario fixo: "))
valor_por_carro = float(input("digite o valor por carro vendido: "))

comissao = carros_vendidos * valor_por_carro
bonus = (5/100) * total_vendas 
salario_final = salario_fixo + comissao + bonus

print(f"o salario final do vendedor e:  {salario_final}")