numeroOriginal = int(input("\nDigite o número: "))

opcao = input("selecionar a forma de " \
"conversaõ: \n1 - Binario :\n2 - Octal" \
"\n3 - Hexadecimal:\n Resultado: ")

if opcao == "1":
	print(f"{numeroOriginal:b}")
elif opcao == "2":
	print(f"{numeroOriginal:o}")
elif opcao == "3":
	print(f"{numeroOriginal:x}")

