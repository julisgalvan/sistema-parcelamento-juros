# SISTEMA DE PARCELAMENTO COM JUROS

# A. Print de boas-vindas com nome e sobrenome
print("Olá bem-vindo a loja do Rodrigo Galvan")

# B. Input do valor do pedido e quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido: R$ "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas desejada: "))

# C. Definindo a taxa de juros conforme a quantidade de parcelas
if quantidadeParcelas < 4:
     juros = 0.00 # 0%
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
     juros = 0.04 # 4%
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
     juros = 0.08 # 8%
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
     juros = 0.16 # 16%
else: # quantidadeParcelas >= 13
      juros = 0.32 # 32%

# D. Cálculo do valor total parcelado e valor da parcela
valorTotalParcelado = valorDoPedido * (1 + juros)
valorDaParcela = valorTotalParcelado / quantidadeParcelas

# Exibição dos resultados
print(f"Resumo do parcelamento:")
print(f"Valor original: R$ {valorDoPedido:.2f}")
print(f"Quantidade de parcelas: {quantidadeParcelas}")
print(f"Valor de cada parcela: R$ {valorDaParcela:.2f}")
print(f"Valor total parcelado: R$ {valorTotalParcelado:.2f}")
