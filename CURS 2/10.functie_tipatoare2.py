
def functie_tipatoare(param, *args, **kargs):
    print(args, type(args))
    print(kargs, type(kargs))

functie_tipatoare(param = 30)
functie_tipatoare(param = 30, mamaliga = 300, branza = 400)