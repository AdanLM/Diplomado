import pickle

with open("diccionario.bin", "rb") as fh:
    aDiccionario = pickle.load(fh)

# Validamos que sea un diccionario
print(type(aDiccionario))
# Imprimimos los valores del diccionario
print(aDiccionario)
print("Done")
