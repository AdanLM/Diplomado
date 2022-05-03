import math

ladoA = 9
ladoB = 8
ladoC = 21

semiPerimeter = (1 / 2) * (ladoA + ladoB + ladoC)

print(semiPerimeter)

aux = ladoA * ladoB * ladoC
aux1 = semiPerimeter * (semiPerimeter - ladoA) * (semiPerimeter - ladoB) * (semiPerimeter - ladoC)
radio = aux / math.sqrt(aux)

print(radio)
