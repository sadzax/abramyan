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

def inputter_int(input_descripton, arg_error, arg_min, arg_max, arg_isnt):
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

def inputter_float(input_descripton, arg_error, arg_min, arg_max, arg_isnt):
    while True:
        try:
            i = float(input(input_descripton))
            if arg_min_f(i, arg_min) is False or arg_max_f(i, arg_max) is False or arg_isnt_f(i, arg_isnt) is False:
                print(arg_error)
                continue
            return i
        except:
            print(arg_error)
            continue

def inputter_float(input_descripton, arg_error, arg_exclude_list):
    while True:
        try:
            i = float(input(input_descripton))
            if type(arg
            for i in arg_exclude_list:
            if arg_min_f(i, arg_min) is False or arg_max_f(i, arg_max) is False or arg_isnt_f(i, arg_isnt) is False:
                print(arg_error)
                continue
            return i
        except:
            print(arg_error)
            continue

