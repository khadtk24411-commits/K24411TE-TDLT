from math import sqrt

def PTbac2(a, b, c):
    if a == 0:
        if b == 0 and c == 0:
            a = "Infinite solutions"
        elif b == 0 and c != 0:
            a = "No solutions"
        else:
            x = round(-c / b, 2)
            a = "x=" + str(x)
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            a = "No solutions"

        elif delta == 0:
            x = round(-b / (2 * a), 2)
            a = "x1=x2=" + str(x)

        else:
            x1 = round((-b - sqrt(delta)) / (2 * a), 2)
            x2 = round((-b + sqrt(delta)) / (2 * a), 2)
            a = "x1=" + str(x1) + " x2=" + str(x2)

    return a