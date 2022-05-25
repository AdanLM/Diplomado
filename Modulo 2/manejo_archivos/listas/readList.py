import pickle

with open("list.bin", "rb") as fh:
    aList = pickle.load(fh)

# Validamos que sea una lista
print(type(aList))
# Imprimimos los valores de la lista
print(aList)
print("Done")