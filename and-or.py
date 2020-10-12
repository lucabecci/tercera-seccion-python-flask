# AND se utiliza para que en una condicion se cumpla dos o mas condiciones, es decir
# si mi primer condicion se cumple tambien quiero que se cumpla la que esta despues del
# and para devolver mi codigo

# Se cumple
if 2 < 5 and 2 > 1: print(True)
# No se cumple
if 2 < 5 and 2 > 3: print(True)

# OR se utiliza para ejecutar nuestro codigo de la condicion segun si alguna de
# las condiciones dadas en nuestra estructura condicional se cumple.

if 1 < 0 or 1 > 0: print(True, 'una de las dos condiciones es verdadera')
# Para que no se ejecute necesitamos que ambas condiciones sean falsas.