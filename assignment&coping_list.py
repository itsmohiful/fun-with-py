list1 = [65,456,54,77]
list2 = list1
print(list2)

list1[0] = 'proton'
print(list2)

list3 = list(list1)     #coping list with constructor
print(list3) 