def dev_dec(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
@dev_dec

def div(a,b):
    #print(a/b)
    #if a<b:
        #a,b=b,a
    return a/b #Perform the division
# Test cases
div(2,4)
#div(4,2)
    #a/b
    #2/4 0.5 # Normal case
#div() # Division by zero case

def dev_dec(func):
    def inner(a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

@dev_dec
def div(a, b):
    return a / b   
print(div(4, 0))