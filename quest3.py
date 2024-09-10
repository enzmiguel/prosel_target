import json  # importa a biblioteca para manipulação de arquivos JSON

# abre o arquivo HIPOTÉTICO de faturamento
with open('faturamento.json', 'r') as arquivo:
    dados = json.load(arquivo)

# filtra os dias que tiveram faturamento (valores maiores que 0)
faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

# encontra o menor valor de faturamento
menor_faturamento = min(faturamentos)

# encontra o maior valor do faturamento
maior_faturamento = max(faturamentos)

# calcula a média de faturamento, (soma dos valores / número de dias)
media_mensal = sum(faturamentos) / len(faturamentos)

# conta quantos dias tiveram faturamento acima da média
dias_acima_da_media = len([valor for valor in faturamentos if valor > media_mensal])

# teste
print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
