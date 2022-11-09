# Begin39
# Найти корни квадратного уравнения A·x2 + B·x + C = 0, заданного своими коэффициентами A, B, C (коэффициент A не равен 0), если известно, 
# что дискриминант уравнения положителен. Вывести внача-ле меньший, а затем больший из найденных корней.

import sadzax

error = "Please enter only floats"
side_a = sadzax.input_float(f"Enter Side A: ",error,None,None,0)
side_b = sadzax.input_float(f"Enter Side B: ",error,None,None,0)
side_c = sadzax.input_float(f"Enter Side C: ",error,None,None,0)

disc = 