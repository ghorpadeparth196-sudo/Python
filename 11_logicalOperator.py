#logical operator = nevaluate multiple conditions (or, and, not)
#                   or = at least one condition must be True
#                   and = both conditions must be True
#                   not = inverts the condition (not False, not True)     

temp =20
is_sunny = False

if temp >= 28 and is_sunny:
    print("it is Hot outside")
    print("it is sunny")
elif temp <= 0 and is_sunny:
    print("it is Cold outside")
    print("it is sunny")
elif temp > 0 and is_sunny:
    print("it is Warm outside")
    print("it is sunny")
elif temp >= 28 and not is_sunny:
    print("it is Hot outside")
    print("it is cloudy")
elif temp <= 0 and not is_sunny:
    print("it is Cold outside")
    print("it is cloudy")
elif 28> temp> 0  and not is_sunny:
    print("it is Warm outside")
    print("it is cloudy")