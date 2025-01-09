"""def square(i):
    for i in range (i):
        i = i+2
        yield i 
square(5)
for i in square(5):
    print(i)    
"""
def sample(func):
    def wrapper(item):
        item = item.upper()
        return func(item)
    return wrapper
@sample
def greet(item):
    return item

result = greet
print(result("hello"))
