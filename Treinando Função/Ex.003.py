def Nota_Alunos(nota1, nota2):
  media = (nota1 + nota2) / 2
  return media

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

resultadoMedia = Nota_Alunos(nota1, nota2)

if resultadoMedia >= 6:
      print("passou")
else:
      print("reprovado")


print(f"Sua média é {resultadoMedia}")