def porcentagem(quant, total):
    return (100*int(quant))/int(total)

eleitores = input("digite o total de eleitores: ")
brancos = input("digite os votos brancos: ")
nulos = input("digite os votos nulos: ")
validos = input ("digite os votos validos: ")

percentual_brancos = porcentagem(brancos, eleitores)
percentual_nulos = porcentagem(nulos, eleitores)
percentual_validos = porcentagem(validos,eleitores)

print(f"percentual de votos brancos: {percentual_brancos} %")
print(f"percentual de votos nulos: {percentual_nulos} %")
print(f"percentual de votos validos: {percentual_validos} %")