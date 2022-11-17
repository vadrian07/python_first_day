#a = 3
#print(a)
#print(type(a))
#b = 3.8
#print(type(b))
#c = 1j
#print(type(c))
#b = int(b)
#print(type(b))
'Comment '
#c = a/b
#print(c)
#print(5=='5')
#print(5==5)
#print (5>=5 and 4<3)
"AND" \
"TRUE AND TRUE => TRUE" \
"TRUE AND FALSE=> FALSE" \
"FALSE AND TRUE => FALSE" \
"FALSE AND FALSE=>FALSE"

"OR" \
"true or true => true" \
"true or false=> true" \
"false or true =>true" \
"false or false=> false"

"""Si asa se pot scrie comentariile
Yes
"""

#print("7 false is or not: ",7 is 7)
#print(1 in [1 , 2, 3])

variabila = 3
print(variabila)
print(variabila==4)

a=1
#a=a+1
a+=4
print(a)
a-=1
print(a)

nr_numere = 3
nr_pere =4
stringul2 = "Ana are " +str(nr_numere)+ " mere"
print(stringul2)
stringul = 'Ana are "3\' sau "3"  mere'
print(stringul)

stringul3="Ana are {} mere si {}pere".format(nr_numere, nr_pere)
print(stringul3)

""" Sau cea mai noua forma de scriere"""
stringul4 = f"Ana are {nr_numere} mere si {nr_pere}pere"
print(stringul4)

"""Liste"""

#print(type(lista))
#lista.append(3)
#ista.append(2)
#lista.append('ceva')
#lista.append(3)
#cate o valoare odata doar..append adauga valori in lista
lista = [3,4,3,[1,'2','element'],'string']
print(lista)
#de preferat ca lista sa aibe acelasi tip de data in ea..deci liste separate daca existe tipuri de date de alt fel
print(len(lista))
print(lista[1])
print(lista[0:5:2])
#de la 0 la 5 din 2 in 2 elemente.
print(lista[:4])
print('lista care te da peste cap',lista[3][2][3])
#selectam elementul 3 adica lista cu 1,2 si element si al doilea element din acea lista cat si indexul 2 din stringul element


"""Tupluri"""
tuplu = (1,)
#daca facem tuplu =(1) #o sa o ia ca int
print(type(tuplu))
#Il putem folosi cu Django..in tipurile de select..si cam atat...mai rarut...
#dictionaru..seturile vor fi folosite muuuult


"""Dictionar"""
dictionar = {"cheie": "valoare","cheie1":"3"}
#print(dictionar)
#print(dictionar['cheie1'])
#print(dictionar.get['cheie2',5])

#pt a adauga valori in dictionar
#1
dictionar['cheie2']=5
dictionar.update({'cheie2':5,"cheie3":2})# avantaj cu .update ca se pot introduce mai multe valori odata..
#asta poate fi folosit cand avem de exemplu un catalog ..cheia 4 reprezinta o materie si valoarea nota
# nu avem trecuta cheia in catalog asa ca trb sa introducem materia
print(dictionar)
print(dictionar.keys())
print(dictionar.values())

"""Seturi"""
seturi = {1,3,'5',3}
print(seturi)
#converrtim lista la seturi
my_list=[1,2,3,4]
print(set(my_list))
#si invers
print(list(set(my_list)))

"""Seturile si listele sunt folosite la prelucrarile de date"""
"""set doaor cand avem valori unice de preferat..si dupa sa le transferam in altceva"""
"""nu putem accesa seturile ca lista
adica..print(seturi[1]) nu va functiona..trb modificata in lista.."""

