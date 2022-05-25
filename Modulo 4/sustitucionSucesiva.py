from math import exp


# Función
def f(x):
    return exp(2 - x) - 7 * x


# Derivada
def d(x):
    return -exp(2 - x) - 7


x0 = 1.5
x1 = x0 - f(x0) / d(x0)
x2 = x1 - f(x1) / d(x1)
x3 = x2 - f(x2) / d(x2)

print('La raiz es ', x3)
