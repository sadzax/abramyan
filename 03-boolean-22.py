# Дано трехзначное число. Проверить истинность высказывания:
# «Цифры данного числа образуют возрастающую или убывающую после-
# довательность».
# ЗАДАНИЕ ПЕРЕРАБОТАНО: дано целое число

import sadzax
# num = sadzax.input_int("a = ","error",1,None,None)

def look_for_orders_in_number(dgt, counter):
    dgt = dgt // 10
    if dgt < 0:
        return counter
    else:
        return counter
        counter += 1
        look_for_orders_in_number(dgt//10, counter)
    

def check(i):
    if (i // 10) < 10:
        if (i % 2) < 10: 
            return True
    else:
        return False

print(look_for_orders_in_number(5000, 0))