# Calcular valor de y usando Interpolacion de Lagrange
#      x, y
p0 = (-2, 4)
p1 = (-1, -2)
p2 = (3, 5)
p3 = (4.3, 11)
x = 7.7


def fn(x, p0, p1, p2, p3):
    a = ((x - p1[0]) / (p0[0] - p1[0]))
    b = ((x - p2[0]) / (p0[0] - p2[0]))
    c = ((x - p3[0]) / (p0[0] - p3[0]))
    result = a * b * c * p0[1]

    a1 = ((x - p0[0]) / (p1[0] - p0[0]))
    b1 = ((x - p2[0]) / (p1[0] - p2[0]))
    c1 = ((x - p3[0]) / (p1[0] - p3[0]))
    result += a1 * b1 * c1 * p1[1]

    a2 = ((x - p0[0]) / (p2[0] - p0[0]))
    b2 = ((x - p1[0]) / (p2[0] - p1[0]))
    c2 = ((x - p3[0]) / (p2[0] - p3[0]))
    result += a2 * b2 * c2 * p2[1]

    a3 = ((x - p0[0]) / (p3[0] - p0[0]))
    b3 = ((x - p1[0]) / (p3[0] - p1[0]))
    c3 = ((x - p2[0]) / (p3[0] - p2[0]))
    result += a3 * b3 * c3 * p3[1]

    return result

y = fn(x, p0, p1, p2, p3)

print("Cuando X=", x, " Y=", y)
