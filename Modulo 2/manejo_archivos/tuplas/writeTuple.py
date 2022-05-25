import pickle
#Uso de tuplas
aTuple = "Chivas", "America", "Pumas", "Santos"

with open("tuple.bin", "wb") as fh:
    pickle.dump(aTuple, fh)

print("Done...")