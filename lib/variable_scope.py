name = "Joe"

def greeting(name):
    ##the parameters of this function is local so it will pick up on Sophie, if we do not provide an argument we will get an argument error
    ##however if we had empty parameters this function would pick up on the global variable name and print out Hello Joe
    print(f"Hello, {name}")
greeting("Sophie")


def function_scope_practice():
    im_trapped_in_this_function = "There is no access to this variable outside of this function"
##cant access this variable outside its function because its local
#print(im_trapped_in_this_function)


##change a the value of a global variable inside of a function with the keyword global, without the key word the global variable will stay the same value
def change_global_variable():
    global name
    name = "Jade"
    print(name)
change_global_variable()


