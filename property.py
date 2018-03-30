'''
property
'''

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    def get_temperature(self):
        return self._temperature

    temperature = property(get_temperature, set_temperature)


class Celsius2:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter  # need to define @property first
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value



    
man = Celsius2()
man.temperature = 55
print(man.to_fahrenheit())

def changeC(cel):  # cel is a reference, change cel in this function will change the object it refer to
    cel.temperature = 66

changeC(man)
print(man.to_fahrenheit())

def changeA(a): # a is a value parameter, change a will not change the parameter it self
    a = a + 10
    print(a)

b = 12
changeA(b)
print(b)

def make_sandwich(bread):
    bread.add('eggs')
    bread = set(['lettuce', 'moya', 'chicken', 'mayo'])

loaf = set(['wheat', 'soda'])
make_sandwich(loaf)
print(loaf)

'''
a decorator in Python is a callable Python object that is used to modify a function, method or class definition. 
The original object, the one which is going to be modified, is passed to a decorator as an argument. 
The decorator returns a modified object, e.g. a modified function, which is bound to the name used in the definition. 


'''

def out_decorator(func):
    def function_wrapper(x):
        print("Before Calling ", func.__name__)
        func(x)
        print("After calling " + func.__name__)
    
    return function_wrapper

def foo(x):
    print("Calling foo with x = " + str(x))

foo("hello")

foo = out_decorator(foo)
foo(43)


@out_decorator
def fooo(x):
    print("Fooo is called with decorator " + str(x))

fooo(99)


# counting function calls with decorators
def call_counter(func):

    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1
# now succ = call_counter(succ)


@call_counter
def mult(x, y=1):
    return x*y + 1

print(succ.calls)

for i in range(10):
    succ(i)

mult(3, 4)
mult(4)

print(mult.calls)
print(succ.calls)


'''
In Python, functions are first-class objects, just like strings, numbers, lists etc. 
This feature eliminates the need to write a function object in many cases. 
Any object with a __call__() method can be called using function-call syntax.

The __call__ method of classes:
We mentioned already that a decorator is simply a callable object that takes a function as an input parameter. 
A function is a callable object, but lots of Python programmers don't know that there are other callable object. 
A callable object is an object which can be used and behaves like a function but might not be a function. 
It is possible to define classes in a way that the instances will be callable objects. 
The __call__ method is called, if the instance is called "like a function", i.e. using brackets.

'''
class Accumulator(object):
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        self.n += x
        return self.n


def funAccumulator(n):
    def inc(x):
        inc.n += x
        return inc.n
    
    inc.n = n
    return inc


def fun2Accumulator(n):
    def inc(x):
        nonlocal n
        n += x
        return n
    return inc

a = Accumulator(9)
print(a(9))  # object of class can be used as a function if class has a __call__ function

b = funAccumulator(9)
print(b(9))  # function object is returned and can be used as a function 

c = fun2Accumulator(9)
print(c(9))
