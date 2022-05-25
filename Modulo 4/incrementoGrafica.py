from decimal import Decimal


def serie(inicio, fin, incremento):
    aux = inicio
    while aux < fin:
        print("{0:.1f}".format(aux))
        aux += incremento


inicio = 1
fin = 10
incremento = Decimal(0.1)
serie(inicio, fin, incremento)
