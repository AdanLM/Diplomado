import math

#Ejercicio "Calcula el radio de un circulo inscrito en un triangulo"

#Lados del triangulo
a = 10
b = 9
c = 18

print("\nRadio de un circulo inscrito en un triángulo dados sus lados a = 9, b = 8, y c = 21.\n")

#Se obtiene el semiperimetro
s = 0.5 * (a + b + c)
r = math.sqrt(s * (s - a) * (s - b) * (s - c)) / s

print("R=", r)
