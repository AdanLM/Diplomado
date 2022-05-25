import pickle
#Uso de listas
aList = ["Chivas", "America", "Pumas", "Santos"]

with open("list.bin", "wb") as fh:
    pickle.dump(aList, fh)

print("Done...")
