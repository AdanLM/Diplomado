# Calcular valor de x usando Interpolacion lineal
#      x, y
p0 = (-4, -2)
p1 = (1, 5)
y = 3.7


def fn(p0, p1, y):
    a = (y - p0[1])
    b = (p1[0] - p0[0]) / (p1[1] - p0[1])
    return b * a + p0[0]


print("Cuando Y=", y, " X=", fn(p0, p1, y))
