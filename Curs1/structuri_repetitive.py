#while True:
#    print("Set instructiuni")
#    break

variabila1 = 1
variabila2 = 3
while variabila1 < variabila2:
    print(variabila2,'rand 8')
    variabila1 +=1
    # trece de 2 ori prin while si dupa cand conditia nmai e adevarata se trece la rand 11
else:
    print(variabila1,'rand 11')
    #while are si versiunea de else..asta ruleaza doar cand while nu e adevarat,,si nu se foloseste asa structura

#while poate fi folosita la trimis email uri..credca si la log ari..

"""Instructiunea for """
"""asa se scrie in python..i e valoare temporala"""
#for i in "Ana are mere":
#    print(i)
#cand dorim sa avem index si valoare..trb sa ne folosim de o functie denumita

#for i, v in enumerate("Ana are mere"):
#    print(i, v)
#acum avem si indexul si valoarea

lista = ["cumparaturi","citit"]
for i, v in enumerate(lista):
    print(i, v)

for i in range(3, 10, 3):
    print(i)
    #output: 3,6,9

dictionar = {"carte": 1, "carte2":2, "carte3":3}
for i in dictionar.items():
    print(i, v)
#ne afiseaza doar cheile pt ca s valorile unice..dictionar.keys()..daca vreau sa iterez prin valorile cheilor..dictionar.values()
#putem si prin dictionar.items()..si afiseaza tuples acum...
# pt a afisa si valoarea si cheia trb print(i, v)
#fiecare element din tuplu este adaugat intro variabila..index si value..

"""dictionar = {"carte": 1, "carte2":2, "carte3":3}
for i in dictionar.items():
    index, value = i
    print(index, value)"""

