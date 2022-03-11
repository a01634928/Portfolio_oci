incremento = 0.3
valor_inicial_x = -1
valor_inicial_y = 6
print('Runge-Kutta de orden 4')
t = 0  #  t es el valor de tiempo inicial

def funcion_f(x, y):
    valor = 2*x + 4*y
    return valor


def funcion_g(x, y):
    valor = -1*x+6*y
    return valor


while t <= 10:
    m1 = funcion_f(valor_inicial_x, valor_inicial_y)
    k1 = funcion_g(valor_inicial_x, valor_inicial_y)

    m2 = funcion_f(valor_inicial_x + (incremento * m1) / 2, valor_inicial_y + (incremento * k1) / 2)
    k2 = funcion_g(valor_inicial_x + (incremento * m1) / 2, valor_inicial_y + (incremento * k1) / 2)

    m3 = funcion_f(valor_inicial_x + (incremento * m2) / 2, valor_inicial_y + (incremento * k2) / 2)
    k3 = funcion_g(valor_inicial_x + (incremento * m2) / 2, valor_inicial_y + (incremento * k2) / 2)

    m4 = funcion_f(valor_inicial_x + (incremento * m3), valor_inicial_y + (incremento * k3))
    k4 = funcion_g(valor_inicial_x + (incremento * m3), valor_inicial_y + (incremento * k3))

    x = valor_inicial_x + (incremento / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
    y = valor_inicial_y + (incremento / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    print('Imprimiendo los valores de x,y en las iteraciones:t= ' + str(t) + ' x= ' + str(x) + ' y= ' + str(y))

    t = t + incremento
    valor_inicial_x = x
    valor_inicial_y = y

#print('función f: ' + str(funcion_f(x, y)))
#print('función g: ' + str(funcion_g(x, y)))

