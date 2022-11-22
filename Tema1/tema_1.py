# HomeWork #1: Declararea unei liste care sa contina elemente: 7,8,9,2,3,1,4,10,5,6(in aceasta ordine)
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Lista mea: ", my_list)
print("In lista gasim ", len(my_list), "elemente.")

# HomeWork #2: Afisarea unei alte liste ordonata ascendent(lista initiala trebuie pastrara in aceasi forma)
print("Lista ordonata ascendent este: ", sorted(my_list))
# doesn't change the list and returns the sorted list.

# HomeWork #3: Afisarea unei liste ordonata descendent(lista initiala trebuie pastrata in aceasi forma)

print("Lista ordonata descendent este:", sorted(my_list, reverse=True))
descending_list = my_list

# HomeWork #4: Afisarea numerelor pare din lista(folosind DOAR slice, alta metoda va fi considerata invalida)
print("Lista mea neschimbata: ", my_list)

# list_sliced_even = sorted(my_list, reverse=True)
# Utilizam scrierea de sus(reverse=True)in momentul in care dorim ca metoda slice sa fie de genu list_sliced_even[::2]
list_sliced_even = sorted(my_list)
print('Numerele pare din Lista ordonata descendent sunt:', list_sliced_even[1::2])

# HomeWork #5: Afisarea numerelor impare din lista(folosind DOAR slice, alta metoda va fi considerata invalida)
list_sliced_odd = sorted(my_list)
print('Numerele impare din Lista ordonata descendent sunt:', list_sliced_odd[::2])

print("Lista mea neschimbata dupa metoda slice: ", my_list)

# HomeWork #6: Afisarea elementelor multipli ai lui 3.
# list_multiple_of_3 = my_list[1::3];
# print("Multipli lui 3 sunt: ", list_multiple_of_3);

multiple_of_3 = sorted(my_list)
print("Folosind metoda slice, multipli lui 3 din lista sunt: ", multiple_of_3[2::3])
