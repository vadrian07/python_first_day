"""Structura decizionala"""
"""Programare conditionala"""
"""Evalueaza mai multe expresii sub forma de true si false.."""
variabila1 = 1
variabila2 = 2
mesaj ="Variabila 1 mai mica" #preluam textul din else si il bagam aici
if variabila1 == variabila2:
    mesaj = 'egalitate'
elif variabila1 > variabila2:
    mesaj = 'Variabila 1 e mai mare'
print(mesaj)
#else: print('variabila 1 e mai mica')
#tool uri ce analizeaza munca..alea zic ca else s ar putea sa nu existe..adicaputem schimba  cu alteceva
mesaj="egalitate" if variabila1 == variabila2 else "variabila 1 e mai mica"
print(mesaj)