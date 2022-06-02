str1 = "hey univers welcome"
print(str1)

print(str1.capitalize())
print(str1.upper())

jonny = "jonny, jonny yes pappa. eating sugar ? no pappa. telling lie ? no pappa. open your mouth. ha ha ha "
print(jonny.count('no'), jonny.count('pappa'))  #count function

str2 = "google.com"
print(str2.endswith('com'))      #endswith function

print(str1.find('y'),"y is in")     #find function
print(len(str1),"length of str1")   #length function
print(str1.split())     #split function
print(str1.split('e'),"splite with e")

swap = "hello wHats is Up?"
print(swap.swapcase())  #swapcase function

print(str1.replace('univers','metavers'))   #replace function

print(str1.isdigit()) #isdigit function

print(str1.isalpha()) #isalpha, space is not alphabet

print(str1.strip('e')) #strip_function, is remove mentioned letter from left & right

print(str1.lstrip('hey')) #left_strip & right _ srtip
print(str1.rstrip('me'))
