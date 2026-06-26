def calculo_hipotenusa(catetoA, catetoB):
  hipotenusa = catetoA**2 + catetoB**2
  resultadoHipo = hipotenusa ** (1 / 2)
  return resultadoHipo

catetoA = int(input("Digite o numero do cateto A: "))
catetoB = int(input("Digite o numero do cateto B: "))

resulHipotenusa = calculo_hipotenusa(catetoA, catetoB)

print(f"\nO valor da hipotenusa é: {resulHipotenusa}")
