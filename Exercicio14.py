macas_compradas= int(input("digite o total de macas compradas:" ))
if macas_compradas >= 12:
    custo_total= macas_compradas * 1.00
else:
    custo_total= macas_compradas * 1.30

print(f"custo total da venda e: {custo_total}")