import pickle

lista = ["a list", "including another list", ["inner", "list"]]

with open('list.bin', 'wb') as fh:
    pickle.dump(lista, fh)

print('done...')
