# If28. Дан номер года (положительное целое число). Определить количество
# дней в этом году, учитывая, что обычный год насчитывает 365 дней, а
# високосный — 366 дней. Високосным считается год, делящийся на 4, за
# исключением тех годов, которые делятся на 100 и не делятся на 400
# (например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000
# — являются).
import sadzax

year = sadzax.Enter.int('enter year: ','error',0,None,None)

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        status = "Not Leap"
    else:
        status = "Leap"
else:
    status = "Not Leap"

if status == "Leap":
    print('366')
elif status == "Not Leap":
    print('365')
else:
    print('undefined')