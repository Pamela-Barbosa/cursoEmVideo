km = float(input("\nDigite a quantidade de kilometros percorrido (Ex: 10km) "))
dias = float(input("Digite a quantidade de dias que ficou com o carro: "))

calKm = km * 0.15
calDias = dias * 60
calcTotal = calKm + calDias

print(f"Você percorreu o total de: {km}km\nE ficou com o carro o por: {dias} dias")
print(f"O total a ser pago pelo carro alugado é: {calcTotal}")