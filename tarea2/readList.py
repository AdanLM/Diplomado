import pickle

with open('list.bin','rb') as fh:
        lista = pickle.load(fh)

print(type(lista))
print(lista)

print('done...')
