# Iniciando os valores de faturamento por estado
fat_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calculandp o valor total de faturamento mensal
total = sum(fat_estado.values())

# calculando o percentual de representação de cada estado
perc = {}
for estado, valor in fat_estado.items():
    perc[estado] = (valor / total) * 100

# imprimindo os resultados
for estado, percentual in perc.items():
    print(f"Representação {estado}: {percentual:.2f}%")