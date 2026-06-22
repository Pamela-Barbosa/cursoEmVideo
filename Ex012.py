produto = float(input("Digite o valor do produto: "))
cal_desc = produto * 0.05
apli_desconto = produto - cal_desc

print("\nVocê recebeu um desconto de 5%  \nO preço final é: {}R$".format(apli_desconto))