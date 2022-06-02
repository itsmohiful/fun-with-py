# list is mutable but tuple is immutable
animals = []
animals = ['dog','cat','monkey','donkey',89,52,43]
print(animals)
print(animals[4])

list1=[[10,20],[30,40]]
print(list1)
print(list1[0])
print(list1[0][1])

for i in [10,20,30,40,50]:
    print(i)

#replace, delete,insert,append,sort,reverse
print("list: replace, delete,insert,append,sort,reverse operations")

list2 = [15,25,35,45]
print(list2)
list2[2]=55
print("replace 55 in 3rd index = ",list2)
list2.insert(2,'hey')
print("insert hey = ", list2)

list3=[3,53,123,78,2,563,2,4]
list3.sort()
print("sorting list: ",list3)

del list3[2]
print("delete index 2 = ",list3)

list3.append('add')
print("append = ",list3)

list3.reverse()
print("reverse = ", list3)



numlist = [40, 100, 1, 5, 25, 10]
numlist.sort()
print("sorting: ", numlist)