# def fun1():
#     print("script kiddie")
    
# var1 = fun1
# del fun1
# var1()    

def fun1(fun):
    def fun2():
        fun()
        print("subscribe to my channel")
    return fun2()

@fun1 #Decorators is used to 
def script():
    print("script kiddie")
    
script()
       