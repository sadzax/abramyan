def arg_min_f(i, arg):
    if arg is not None:
        if i < arg:
            return False
    else:
        return True

def arg_max_f(i, arg):
    if arg is not None:
        if i > arg:
            return False
    else:
        return True

def arg_isnt_f(i, arg):
    if arg is not None:
        if i == arg or arg is True:
            return False
    else:
        return True

def arg_isnt_in_list_f(i, arg):
    if arg is not None:
        if isinstance(arg, (list, tuple)):
            for el in arg:
                if el == i:
                    return False
        elif i == arg or arg is True:
            return False
    else:
        return True
 
def input_int(input_descripton, arg_error, arg_min, arg_max, arg_isnt):
    while True:
        try:
            i = int(input(input_descripton))
            if arg_min_f(i, arg_min) is False or arg_max_f(i, arg_max) is False or arg_isnt_f(i, arg_isnt) is False:
                print(arg_error)
                continue
            return i
        except:
            print(arg_error)
            continue

def input_float(input_descripton, arg_error, arg_min, arg_max, arg_isnt_in_list):
    while True:
        try:
            i = float(input(input_descripton))
            if arg_min_f(i, arg_min) is False or arg_max_f(i, arg_max) is False or arg_isnt_in_list_f(i, arg_isnt_in_list) is False:
                print(arg_error)
                continue
            return i
        except:
            print(arg_error)
            continue

def input_str(input_descripton, arg_error, arg_min, arg_max, arg_isnt_in_list):
    while True:
        try:
            i = str(input(input_descripton))
            if arg_min_f(i, arg_min) is False or arg_max_f(i, arg_max) is False or arg_isnt_in_list_f(i, arg_isnt_in_list) is False:
                print(arg_error)
                continue
            return i
        except:
            print(arg_error)
            continue