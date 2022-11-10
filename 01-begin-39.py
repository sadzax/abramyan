# Begin39
# Найти корни квадратного уравнения A·x2 + B·x + C = 0, 
# заданного своими коэффициентами A, B, C (коэффициент A не равен 0), 
# если известно, что дискриминант уравнения положителен. 
# Вывести внача-ле меньший, а затем больший из найденных корней.

import sadzax
import math

error = "Please enter only digits"
while True:
    a = sadzax.input_float(f"Enter A: ",error,None,None,0)
    b = sadzax.input_float(f"Enter B: ",error,None,None,None)
    c = sadzax.input_float(f"Enter C: ",error,None,None,None)
    disc = (b ** 2) - (4 * a * c)
    if disc < 0:
        print('discriminant must be positive, try again')
        continue
    if disc >= 0:
        break

x1 = ((b * -1) - math.sqrt(disc)) / (2 * a)
x2 = ((b * -1) + math.sqrt(disc)) / (2 * a)
answers = sorted([x1, x2])

print(answers)