## 1.Sentencia if

El if es una sentencia condicional que nos permite ejecutar cierto código dependiendo de si se cumple la condición dada. 

*Formas de uso del if:*

```python
if 2 < 5:
    print('2 es menor que 5')
#Iniciamos el if como en la primer linea

#La condicion seria 2 < 5 donde condicionamos al if con la pregunta de si
# 2 es menor a 5

#Si esto se cumple se mostrara por console 2 es menor que 5, pero 
#si no se cumple el codigo seguira sin mostrar eso por consola.
```

*Operadores utilizados para condicionales*:

```python
# a == b evaluamos si ambas variables son iguales
# a > b evaluamos si a es mayor a b
# a < b evaluamos si a es menor que b
# a != b evaluamos si a es distinto a b
# a <= b evaluamos si a es menor o igual a b
# a >= b evaluamos si a es mayor o igual a b
```

```python
if 2 == 2:
    print('2 es igual a 2')

if 2 == 3:
    print('2 es igual a 3')

if 2 > 5:
    print('2 es mayor a 5')

if 2 < 5:
    print('2 es menor a 5')

# Y asi con los demas...
```

## 2. elif, else

### elif

 

El elif se utiliza en el caso de que la primer condición no se cumpla, y se evalúa la del elif para ver si su condición se puede ejecutar. Si la primera es verdadera no se ejecutara el elif ya que termina en la primer condición. Este mismo podemos utilizarlo todas las veces que queramos.

```python
 if 2 > 6:
     print('2 es mayor que 6')
 elif 2 < 5: 
     print('2 es menor a 5 en elif')
#Se ejecuta el elif ya que es la primer condicion es falsa
# y la segunda (elif) si es verdadera.
```

### else

El else se utiliza en el caso de que ninguna condición se cumpla, es decir, si no se cumple ninguna de mis condiciones quiero que ejecutes ese código => "NUESTRO CÓDIGO A EJECUTAR".

```python
if 2 > 6:
    print('2 es mayor que 6') #falsa
elif 2 < 1: 
    print('2 es menor a 5 en elif') #falsa
else: 
    print('aparezco si todas las condiciones anteriores son falsas')

if 1 != 1:
    print(False)#falsa
else: 
    print(True)
```

## 3. Condicional if de forma corta y if con ternario

### if corto:

Si nosotros quisiéramos hacer un if de una sola linea ya que nuestro código

a ejecutar en el if puede ser corto tendríamos que:

```python
if 1 == 1: print('x')
```

### Condicional if con ternario:

Los ternarios son condiciones de una sola linea, se utilizan para cuando queremos evaluar en una sola linea algo y lo que queremos devolver según su boolean.

```python
print(True) if 2 >= 2 else print(False)
```

## 4. and y or

### operador and:

el operador *and* se utiliza para que en una estructura condicional se cumpla dos o mas condiciones, es decir si mi primer condición se cumple también quiero que se cumpla la que esta después del *and* para devolver mi código

```python
# Se cumple
if 2 < 5 and 2 > 1: print(True)
# No se cumple
if 2 < 5 and 2 > 3: print(True)
```

### operador or:

OR se utiliza para ejecutar nuestro código de nuestra estructura condicional según si alguna de las condiciones dadas en esta se cumple.

```python
if 1 < 0 or 1 > 0: print(True, 'una de las dos condiciones es verdadera')
# Para que no se ejecute necesitamos que ambas condiciones sean falsas.
```