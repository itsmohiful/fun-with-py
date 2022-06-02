#local variable

n = 20  #assign global variable

def func1():
    n = 5
    print('local n value is',n)


def func2():
    global n    #declare global variable
    print("global n value is: ",n)
    n = 10 
    print('local n value is: ' , n)
    func1()

func2()
