# Дано трехзначное число. Проверить истинность высказывания:
# «Цифры данного числа образуют возрастающую или убывающую после-
# довательность».

import sadzax
num = sadzax.input_int("a = ","error",1,None,None)

def check(i):
    if (i // 10) < 10:
        if (i % 2) < 10: 
            return True
    else:
        return False

print(check(num))