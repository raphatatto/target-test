import json

with open('target3.json', 'r') as arquivo:
    target3 = json.load(arquivo)

valores = [item['valor'] for item in target3 if item['valor'] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = [item['dia'] for item in target3 if item['valor'] > media_mensal]

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {len(dias_acima_da_media)}")
