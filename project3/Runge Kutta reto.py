incremento = 1
valor_inicial_x = 2.012868
valor_inicial_y =  0.000564
valor_inicial_z =  0.006130
print('Runge-Kutta de orden 4 reto')
t = 0  #  t es el valor de tiempo inicial
#  funcion_f = caribues pm = 28.80 + 15.362 Caribúes rc + 218.4 Coyotes rc + 70.80 Lobos rc
#  funcion_g = coyotes pm = 0.418 + 0.7954 Caribúes rc - 12.57 Coyotes rc + 4.950 Lobos rc
#  funcion_h = lobos pm = 1.2668 - 0.6219 Caribúes rc + 9.407 Coyotes rc + 2.284 Lobos rc


def funcion_f(x, y, z):
    valor = 28.80 + 15.362 * x + 218.4 * y + 70.80 * z
    return valor


def funcion_g(x, y, z):
    valor = 0.418 + 0.7954 * x - 12.57 * y + 4.950 * z
    return valor


def funcion_h(x, y, z):
    valor = 1.2668 - 0.6219 * x + 9.407 * y + 2.284 * z
    return valor


while t <= 50:
    m1 = funcion_f(valor_inicial_x, valor_inicial_y, valor_inicial_z) #* incremento
    k1 = funcion_g(valor_inicial_x, valor_inicial_y, valor_inicial_z) #* incremento
    n1 = funcion_h(valor_inicial_x, valor_inicial_y, valor_inicial_z) #* incremento
    print("m1: " + str(m1))
    print("k1: " + str(k1))
    print("n1: " + str(n1))

    m2 = funcion_f(valor_inicial_x + m1 / 2, valor_inicial_y + k1 / 2, valor_inicial_z + n1 / 2) #* incremento
    k2 = funcion_g(valor_inicial_x + m1 / 2, valor_inicial_y + k1 / 2, valor_inicial_z + n1 / 2) #* incremento
    n2 = funcion_h(valor_inicial_x + m1 / 2, valor_inicial_y + k1 / 2, valor_inicial_z + n1 / 2) #* incremento
    print("m2: " + str(m2))
    print("k2: " + str(k2))
    print("n2: " + str(n2))

    m3 = funcion_f(valor_inicial_x + m2 / 2, valor_inicial_y + k2 / 2, valor_inicial_z + n2 / 2) #* incremento
    k3 = funcion_g(valor_inicial_x + m2 / 2, valor_inicial_y + k2 / 2, valor_inicial_z + n2 / 2) #* incremento
    n3 = funcion_h(valor_inicial_x + m2 / 2, valor_inicial_y + k2 / 2, valor_inicial_z + n2 / 2) #* incremento

    m4 = funcion_f(valor_inicial_x + m3, valor_inicial_y + k3, valor_inicial_z + n3) #* incremento
    k4 = funcion_g(valor_inicial_x + m3, valor_inicial_y + k3, valor_inicial_z + n3) #* incremento
    n4 = funcion_h(valor_inicial_x + m3, valor_inicial_y + k3, valor_inicial_z + n3) #* incremento

    x = valor_inicial_x + (1 / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
    y = valor_inicial_y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    z = valor_inicial_z + (1 / 6) * (n1 + 2 * n2 + 2 * n3 + n4)

    print('Imprimiendo los valores de x,y,z en las iteraciones:t= ' + str(t) + ' x= ' + str(x) + ' y= ' + str(y) + ' z= ' + str(z))

    t = t + incremento
    valor_inicial_x = x
    valor_inicial_y = y
    valor_inicial_z = z

#print('función f: ' + str(funcion_f(x, y)))
#print('función g: ' + str(funcion_g(x, y)))

'''
while t <= 50:
    m1 = funcion_f(valor_inicial_x, valor_inicial_y, valor_inicial_z)
    k1 = funcion_g(valor_inicial_x, valor_inicial_y, valor_inicial_z)
    n1 = funcion_h(valor_inicial_x, valor_inicial_y, valor_inicial_z)

    m2 = funcion_f(valor_inicial_x + (incremento * m1) / 2, valor_inicial_y + (incremento * k1) / 2, valor_inicial_z + (incremento * n1) / 2)
    k2 = funcion_g(valor_inicial_x + (incremento * m1) / 2, valor_inicial_y + (incremento * k1) / 2, valor_inicial_z + (incremento * n1) / 2)
    n2 = funcion_h(valor_inicial_x + (incremento * m1) / 2, valor_inicial_y + (incremento * k1) / 2, valor_inicial_z + (incremento * n1) / 2)

    m3 = funcion_f(valor_inicial_x + (incremento * m2) / 2, valor_inicial_y + (incremento * k2) / 2, valor_inicial_z + (incremento * n2) / 2)
    k3 = funcion_g(valor_inicial_x + (incremento * m2) / 2, valor_inicial_y + (incremento * k2) / 2, valor_inicial_z + (incremento * n2) / 2)
    n3 = funcion_h(valor_inicial_x + (incremento * m2) / 2, valor_inicial_y + (incremento * k2) / 2, valor_inicial_z + (incremento * n2) / 2)

    m4 = funcion_f(valor_inicial_x + (incremento * m3), valor_inicial_y + (incremento * k3), valor_inicial_z + (incremento * n3))
    k4 = funcion_g(valor_inicial_x + (incremento * m3), valor_inicial_y + (incremento * k3), valor_inicial_z + (incremento * n3))
    n4 = funcion_h(valor_inicial_x + (incremento * m3), valor_inicial_y + (incremento * k3), valor_inicial_z + (incremento * n3))
'''