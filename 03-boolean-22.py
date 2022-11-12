# Дано трехзначное число. Проверить истинность высказывания:
# «Цифры данного числа образуют возрастающую или убывающую после-
# довательность».
import sadzax

a = sadzax.Enter.int('a = ','3-digit int only',None,None,None)

def find_digits_and_print_them_out(dgt, lst):
    dgt = abs(int(dgt))
    lst = list(lst)
    if dgt <= 0:
        return lst
    else:
        lst.append(int(dgt % 10))
        return find_digits_and_print_them_out(dgt // 10, lst)

list_1 = find_digits_and_print_them_out(a, [])
list_2 = list_1.copy()
list_2.reverse()

def list_checker(lst, counter):
    lst = list(lst)
    if len(lst) <= (counter + 1):
        return True
    else:
        if lst[counter] < lst[counter + 1]:
            return list_checker(lst, counter + 1)
        else:
            return False

if list_checker(list_1, 0) is True or list_checker(list_2, 0) is True:
    print(True)
else:
    print(False)