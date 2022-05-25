import pickle

with open("tuple.bin", "rb") as fh:
    aTuple = pickle.load(fh)

# Validamos que sea una tupla
print(type(aTuple))
# Imprimimos los valores de la tupla
print(aTuple)
print("Done")
