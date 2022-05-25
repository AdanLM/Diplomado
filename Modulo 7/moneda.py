import random

caras = ['sello', 'aguila']

sello = 0
aguila = 0
repeticiones = 10

for n in range(repeticiones):
    tiro = random.choice(caras)
    if tiro == 'aguila':
        aguila += 1
    else:
        sello += 1

print("Total Aguila: ", aguila)
print("Total Sello: ", sello)
