print("hello");
#instructiune:print("hello");
print(3*3);
#Data types:
# Numbers: Integer(int), Floating(float)
# Strings (Str)
# Lists(list) Ordered sequence of objects: [10,"hello",200.3]
# Dictionaries(dict) Unordered Key: Value pairs: {"mykey":"value","name":"Frankie"}
# Tuples(tup) Ordered immutable sequence of objects (10,"hello",200.3)
# Sets (set) Unordered collection of unique objects: {"a","b"}
# Booleans(bool) Logical value indicating True or False

# Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed over time,
# then it is known as immutable. Once created, the value of these objects is permanent.









#HomeWork #1: Declararea unei liste care sa contina elemente: 7,8,9,2,3,1,4,10,5,6(in aceasta ordine)
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6];
print("Lista mea: ", my_list);
print("In lista gasim ", len(my_list), "elemente.");

#HomeWork #2: Afisarea unei alte liste ordonata ascendent(lista initiala trebuie pastrara in aceasi forma)
print("Lista ordonata ascendent este: ", sorted(my_list));
#doesn't change the list and returns the sorted list.

#HomeWork #3: Afisarea unei liste ordonata descendent(lista initiala trebuie pastrata in aceasi forma)

print("Lista ordonata descendent este:", sorted(my_list, reverse=True));

#HomeWork #4: Afisarea numerelor pare din lista(folosind DOAR slice, alta metoda va fi considerata invalida)
print("Lista mea neschimbata: ", my_list);
#a[start:stop]  # items start through stop-1
#a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array

list_sliced = my_list[-1:-3];
print("Numerele pare din lista sunt: ", list_sliced);

#HomeWork #5: Afisarea numerelor impare din lista(folosind DOAR slice, alta metoda va fi considerata invalida)
list_sliced_impar = my_list[::3];
print("Numerele impare din lista sunt: ", list_sliced_impar);

#HomeWork #6: Afisarea elementelor multipli ai lui 3.
list_multiple_of_3 = my_list[1::3];
print("Multipli lui 3 sunt: ", list_multiple_of_3);