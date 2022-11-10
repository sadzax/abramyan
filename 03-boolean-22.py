# Дано трехзначное число. Проверить истинность высказывания:
# «Цифры данного числа образуют возрастающую или убывающую после-
# довательность».
# ЗАДАНИЕ ПЕРЕРАБОТАНО: дано целое число, нужно взять все его цифры и выложить 
# отсортированным списком. Например, 15486 = 1 4 5 6 8

import sadzax
# num = sadzax.input_int("a = ","error",1,None,None)

def check(i):
    if (i // 10) < 10:
        if (i % 2) < 10: 
            return True
    else:
        return False

def func(d, c, l):
    d = abs(d)
    l = list(l)
    if d <= 0:
        print(l)
        return
    else:
        l.append(int(d % 10))
        func(d // 10, c + 1, l)

func (1898755698, 0, [])

print(len(str(5671)))

def func2(s, c):
    s = str(s)
    if len(s) < 2 or c == 0:
        return
    else:
        s = sadzax.Trimmer.left(s, len(s)-c)
        print(s)
        func2(s, c)

func2 ('Marat Ramazanov', 1)

