precoProduto = float(input("\nDigite o preço do produto: "))

formaPagamento = input("selecionar a forma de " \
"pagamento: \n1 - Dinheiro ou cheque:\n2 - Cartão" \
"\n3 - Em duas parcelas, S/juros\n4 - Em três parcelas C/juros de 20%\nEscolha: ")

if formaPagamento == "1":
	dinheiroCheque = precoProduto - (precoProduto * 0.10)
	print(f"Você recebeu um desconto de 10%, valor final: {dinheiroCheque}R$")

elif formaPagamento == "2":
	cartao = precoProduto - (precoProduto * 0.05)
	print(f"Você recebeu um desconto de 5%, valor final: {cartao}R$")
elif formaPagamento == "3":
	print(f"Você pagou o valor inteiro, preço final: {precoProduto}R$")
else:
	tres_parcelas = precoProduto + (precoProduto * 0.20)
	print(f"Você pagou com 20% de juros, valor final: {tres_parcelas}R$")
