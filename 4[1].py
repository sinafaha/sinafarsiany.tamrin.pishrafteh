def slope(x1, x2, y1, y2):
    return round((y2-y1)/ (x2-x1), 2)


def get_point():
    x = int(input("Please enter x axis:"))
    y = int(input("Please enter y axis:"))
    return x,y


p1 = get_point()
p2 = get_point()
m = slope(p1[0], p2[0], p1[1], p2[1])


def get_b(p, m):
    return p[1] - m*p[0]


b = get_b(p1, m)


def equation(m, b):
    eq = str(m) + "x + " + str(b)
    return eq


print(equation(m, b))
