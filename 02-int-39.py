# Даны целые положительные числа A, B, C. На прямоугольнике раз-
# мера A × B размещено максимально возможное количество квадратов со
# стороной C (без наложений). Найти количество квадратов, размещенных
# на прямоугольнике, а также площадь незанятой части прямоугольника.

import sadzax

a = sadzax.input_int("enter a: ","Only ints!",1,None,None)
b = sadzax.input_int("enter b: ","Only ints!",1,None,None)

while True:    
    c = sadzax.input_int("enter c: ","Only ints!",1,None,None)
    if c > a or c > b:
        print(f'"c" must be under "a" and "b"')
        continue
    else:
        break

Q = (a // c) * (b // c)
P = (a * b) - (Q * c * c)

print(Q)
print(P)