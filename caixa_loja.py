# Desafio: Sistema de Caixa de Loja
# Crie um programa que simule o caixa de uma pequena loja. 
# O sistema deve:
# Pedir o nome do cliente. 
# Usar um loop while para registrar os produtos: 
# O usuário digita o nome do produto e seu preço. 
# O programa pergunta se deseja adicionar outro produto ou finalizar a compra. 
# Usar uma lista para armazenar os produtos comprados. 
# Ao final da compra, mostrar: 
# A lista de produtos e preços 
# O valor total 
# Se o total for maior que R$ 100, aplicar 10% de desconto (usar if) 
# Usar um for para exibir os produtos com seus valores. 
# Imprimir a mensagem final de agradecimento com o nome do cliente.

nome_cliente = str(input("Informe seu nome: "))
add_produto = True

produtos_comprados = []
total = 0
desconto = 10
total_desconto = 0

while add_produto == True:
  produto = str(input("Informe o produto: "))
  produtos_comprados.append(produto)

  preco = float(input("Informe o preço do produto: "))
  produtos_comprados.append(preco)
  total += preco

  add_produto = str(input("Deseja inculir outro produto no carrinho? "))
  if add_produto == "sim":
    add_produto = True

for item in range(0, len(produtos_comprados), 2):
  print(f"Produto: {produtos_comprados[item]} - Preço {produtos_comprados[item+1]}")
  
if total > 100:
  total_desconto = total * (1 - desconto / 100)
  print(f"O valor total é de: R${total:.2f}. Com o desconto aplicado, o valor atualizado é R${total_desconto:.2f}.")
else:
  print(f"O valor total é de R${total:.2f}.")

print(f"{nome_cliente}, agradecemos a preferência. Volte sempre.")



