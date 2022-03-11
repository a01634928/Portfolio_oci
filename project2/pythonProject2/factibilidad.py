cantidad_inicial = 0
deposito = 50000
monto_generado = 0
cantidad_final = deposito
#2363798.46   36meses
contador  = 0
while cantidad_final < 2363798.46:
    contador += 1
    cantidad_inicial = round(cantidad_final, 3)
    monto_generado = round(cantidad_inicial * 1.01, 3)
    cantidad_final = round(deposito + monto_generado, 3)
    print('Mes: '+ str(contador) +' Cantidad inicial: ' + str(cantidad_inicial) + ' ------ Monto generado: ' + str(monto_generado) + ' ------ Cantidad Final: ' + str(cantidad_final))
