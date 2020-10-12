# El elif se utiliza en el caso de que la primer condicion no se cumpla, y se evalua la del elif
# para ver si su condicion se puede ejecutar. Si la primera es verdadera no se ejecutara el elif ya que termina
# en la primer condicion. Este mismo podemos utilizarlo todas las veces que queramos.
# if 2 > 6:
#     print('2 es mayor que 6')
# elif 2 < 5: 
#     print('2 es menor a 5 en elif')

#El else se utiliza en el caso de que ninguna condicion se cumpla, es decir, si no se cumple ninguna
# de mis condiciones quiero que ejecutes ese codigo => "NUESTRO CODIGO A EJECUTAR".

if 2 > 6:
    print('2 es mayor que 6')
elif 2 < 1: 
    print('2 es menor a 5 en elif')
else: 
    print('aparezco si todas las condiciones anteriores son falsas')

if 1 != 1:
    print(False)
else: 
    print(True)