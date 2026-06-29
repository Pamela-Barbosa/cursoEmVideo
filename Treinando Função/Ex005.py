def tabuada(num2):
    contador = 1 

    while contador <= 10:
        mult = num2 * contador
        print(f"{num2} x {contador} = {mult}")
        
        contador += 1
        
    return "Tabuada concluída!"

print(tabuada(8))

