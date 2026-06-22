import math

angulo = int(input("\nDigite um angulo (30)°: "))

radianos = math.radians(angulo)

sen = math.sin(radianos)
cos = math.cos(radianos)
tan = math.tan(radianos)

print(f"O Grau digitado é: {angulo}°")
print(f"Seno é: {sen:.4f} ")
print(f"Cosseno é: {cos:.4f} ")
print(f"Tangente é: {tan:.4f} ")
