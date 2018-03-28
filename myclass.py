'''
https://docs.python.org/3.6/tutorial/classes.html

As is true for modules, classes partake of the dynamic nature of Python: 
they are created at runtime, and can be modified further after creation.

class members (including the data members) are public (except Private Variables), 
and all member functions are virtual.

there are no shorthands for referencing the object’s members from its methods: 
the method function is declared with an explicit first argument representing the object, 
which is provided implicitly by the call.

As in Smalltalk, classes themselves are objects.

Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. 
This is known as aliasing in other languages

When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance. 

'''

def scope_test():
    def do_local():
        spam = "local spam"
        print(spam)

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        print(spam)

    def do_global():
        global spam
        spam = "global spam"
        print(spam)

    spam = "test spam"
    do_local()
    print("after local assignment: ", spam)

    do_nonlocal()
    print("after nonlocal assignment: ", spam)

    do_global()
    print("after global assignment: ", spam)

scope_test()
print("In global scope: ", spam)


class Complex:

    kind = 'Complex number'    # class variable shared by all instances, like static variable in c#

    def __init__(self, realpart, imagpart):
        self.r = realpart      # instance variable unique to each instance
        self.i = imagpart      # instance variable unique to each instance

x = Complex(3.0, -4.5)

print(x.r)
print(x.i)

x.counter = 1  # data attributes correspond to “instance variables” in Smalltalk, and to “data members” in C++
               # like local variables, they spring into existence when they are first assigned to. 
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

'''
“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. 
However, there is a convention that is followed by most Python code: 
a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API 
(whether it is a function, a method or a data member). 
It should be considered an implementation detail and subject to change without notice.

name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) 
is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) 
stripped. This mangling is done without regard to the syntactic position of the identifier, 
as long as it occurs within the definition of a class.
'''
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubClass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


y = Mapping([1,2,3])
# y.__update([4,5,6]) # this is wrong, but below is correct, and should not be used
y._Mapping__update([4,5,6])
print(y.items_list)


print(__name__)   # if this script is imported by other scripts as a module, then the value is 'myclass'
                  # if this script is run directly: python myclass.py 33.0 22.0 , then the value is '__main__'

if __name__ == "__main__":
    import sys
    z = Complex(sys.argv[1], sys.argv[2])
    print(z.r)
    print(z.i)