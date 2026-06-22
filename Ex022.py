numeros = int(input("\nDigite um número de: 0 a 9999: "))
unidade = numeros % 10
dezena = (numeros // 10) % 10
centena = ((numeros // 100) % 10)
milhar = ((numeros // 1000) % 10) #Aqui divide primeiro o numero, e depois verifica o resto

print(f"A unidade do {numeros} é: {unidade}")
print(f"A dezena do {numeros} é: {dezena}")
print(f"A centena do {numeros} é: {centena}")
print(f"O milhar do {numeros} é: {milhar}")