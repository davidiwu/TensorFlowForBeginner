'''
https://docs.python.org/3.6/tutorial/modules.html

A module can contain executable statements as well as function definitions. 
These statements are intended to initialize the module. 
They are executed only the first time the module name is encountered in an import statement. 
(They are also run if the file is executed as a script.)

When a module named spam is imported, the interpreter first searches for a built-in module with that name. 
If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path. 
sys.path is initialized from these locations:

1. The directory containing the input script (or the current directory when no file is specified).
2. PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
3. The installation-dependent default.


The __init__.py files are required to make Python treat the directories as containing packages; 
this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. 
In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable

https://stackoverflow.com/questions/19077381/what-happens-when-i-import-module-twice-in-python

if a module has already been imported, it's not loaded again.
You will simply get a reference to the module that has already been imported (it will come from sys.modules).
To get a list of the modules that have already been imported, you can look up sys.modules.keys()

if you want to reload it, use: imp.reload()
'''
# from myclass import Complex as Comp
import myclass
import sys

print(myclass.__name__)
print(sys.path)

x = myclass.Complex(4.0, -5.6)

print(x.r)
print(x.i)



print(__name__)   # if this script is imported by other scripts as a module, then the value is 'modules'
                  # if this script is run directly: python modules.py 33.0 22.0 , then the value is '__main__'
if __name__ == "__main__":
    import sys
    gg = myclass.Complex(sys.argv[1], sys.argv[2])
    print(gg.r)
    print(gg.i)