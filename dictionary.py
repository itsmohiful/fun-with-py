#dictionary is associated data type which value is in some refarrence (key:value)
test_dict ={
    'name':'scorpion',
    'email':'mohiful.islam.ofc@gmail.com',
    'mobile':'01856752327'
}
print(test_dict)

print(test_dict['email'])

#coping dictionary
test_dict_2 = dict(test_dict) #copy
print(test_dict_2)


print(len(test_dict)) #length

del(test_dict['mobile']) #delete
print(test_dict)

print(test_dict.keys()) #all keys
print(test_dict.values()) #all values

# print("access by dots: ",test_dict.name)