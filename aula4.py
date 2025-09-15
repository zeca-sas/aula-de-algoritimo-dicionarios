import random

vendas = {f"dia {i+1}": random.randint(0, 50) for i in range(30)}
print(vendas)

dia_max = max(vendas, key=vendas.get)
dia_min = min(vendas, key=vendas.get)

print(dia_max,"com mais vendas")
print(dia_min,"com menos vendas")

media = sum(vendas.values()) / len(vendas)
print(f"Média de vendas: {media:.2f}")


acima_da_media = {dia: qtd for dia, qtd in vendas.items() if qtd > media}
print("Dias com vendas acima da média:", acima_da_media)