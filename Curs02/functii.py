def functie_1(param_1, param_2, *args, **kwargs):
    print(type(args))
    print(type(kwargs))
    suma = 0
    suma = param_1 + param_2
    for i in args:
        suma += i
    for i in kwargs.values():
        suma += i
    return suma
print(functie_1(1, 5, 4, 5, v=3, c=6))
