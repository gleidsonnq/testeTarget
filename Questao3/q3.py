import json

# Abre o arquivo dados.json e carrega os dados em um dicionário
with open("dados.json") as arquivo:
    dados = json.load(arquivo)

# Inicializa a variável faturamento
faturamento = []

# Coletando valores dos dias com faturamento
for dia in dados:
    if dia["valor"] != 0:
        faturamento.append(dia["valor"])

# Calculando a media
media = sum(faturamento) / len(faturamento)

# Calculando o menor faturamento
menor_fat = min(faturamento)

# Calculando o maior faturamento
maior_fat = max(faturamento)

# Calculando o numero de dias de faturamento acima da media
dias_sup_media = 0
for valor in faturamento:
    if(valor>media):
        dias_sup_media+=1

print(f"Menor valor de faturamento: {menor_fat:.2f}")
print(f"Maior valor de faturamento: {maior_fat:.2f}")
print(f"Numero de dias com faturamento acima da media: {dias_sup_media}")
