def test_func(*mylist):     #function declare
    for i in mylist:
        print(i)
    return


print('first excecute')
test_func(5,6,2,8,45,4)     #run_function


print('2nd excecute')
test_func(9,5)     #run_function


print('3rd excecute')
test_func(4,6,34,6)     #run_function