name = 'scorpion'
list1=[23,65,34,762,93,42,88]
tuple1=(34,76,13,87,56,78)

print("lenght name",len(name)) #length
print("lenght list",len(list1))
print("lenght tuple",len(tuple1))

print(name[1:5]) #slice
print(list1[2:]," & " , list1[:4], " & ", list1[1:2:5])

name.count('o')#count
b='c' not in name #membership
print(b)
c='islam'
d=name+c #concatenation
print(d)

list2=[34,53,235,6,6]

m = list1 + list2
print(m)

print(min(m)) #min value
print(max(m)) #max value

print(sum(m)) #sum function