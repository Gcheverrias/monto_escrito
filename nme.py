                        #prueba de monto Escrito 
monto_escrito=(str(' ***'))
unidad_des=['un',' uno',' dos',' tres',' cuatro',' cinco',' seis',' siete',' ocho',' numeve',' diez',' once',' doce',' trece',' catorce',' quince']
decena_des=['i','diez',' veinte',' treinta',' cuarenta',' cincuenta',' sesenta',' setenta',' ochenta',' noventa']
centena_des=[' cien',' ciento',' doscientos',' trescientos',' cuatrocientos',' quinientos',' seiscientos',' setecientos',' ochocientos',' novecientos']
nro = 0
unidad = 0
decena = 0
centena = 0
uni_dec = 0
numero=(str(0))
nro = int(input ("Ingrese un numero de tres digitos: "))
if nro == 0:
    print: ("numero es cero o blanco")
else:

    numero = (str(nro))
    numero = (list(numero.zfill(3)))
    unidad = int(numero[2])
    decena = int(numero[1])
    centena = int(numero[0])
    uni_dec = int(numero[1]+numero[2])
pass
print ('El numero ingresado es:',nro)
#
# RUTINAS DE CONSTRUCCION DEL MONTO ESCRITO
#              centenas
if nro == 100:
        monto_escrito += centena_des[0]    #  CIEN
elif nro > 100:
        monto_escrito += centena_des[centena]    # CIENTOS SELECCIONADOS DE CIENTO A NOVECIENTOS
pass 
                # decenas
if uni_dec == 0:
        monto_escrito += ','
elif uni_dec > 15:
    if decena == 0:
        monto_escrito = monto_escrito
    else:
        monto_escrito += (decena_des[decena])
    pass
elif uni_dec < 16:
        monto_escrito += (unidad_des[uni_dec])
pass
# unidades
if unidad > 0:
    if uni_dec > 15:
        monto_escrito += (" y" + unidad_des[unidad])
    pass
pass
print ('-'*50)
print (monto_escrito,'***')
print ('-'*50)

