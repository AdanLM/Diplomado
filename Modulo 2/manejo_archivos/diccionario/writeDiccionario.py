import pickle
#Uso de listas
aDiccionario = {"12": "Chivas", "13":"America", "11":"Pumas", "6": "Santos"}

with open("diccionario.bin", "wb") as fh:
    pickle.dump(aDiccionario, fh)

print("Done...")
