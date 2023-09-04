custo_fabrica = input ("digite o custo de fabrica: ")
valor_dist = float(custo_fabrica) * 0.28
valor_imp = float(custo_fabrica) * 0.45
custo_final = float(custo_fabrica) + valor_dist + valor_imp

print(f"custo final do consumidor: {custo_final}")