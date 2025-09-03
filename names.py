import string

#------------------------------------------------------------------------------
# In this section, define a function that returns your name

def james():
    def f(x): return (24*x**4 - x**3 + 5*x**2 - 8*x + 9) % 29
    return ''.join(string.ascii_lowercase[f(n)] for n in range(5)).capitalize()

def mario():
    start: int = 100
    jumps: list[int] = [9, -3, 14, 5, 11, -1, 11, 0, 1, 15, 2, 11, 14, 2, 17, 10]
    return ''.join(chr(start + j) for j in jumps).capitalize()

def hasib():
    values = [72, 97, 115, 105, 98]
    return ''.join(chr(v) for v in values)

def jian():
    Tindex=[74,73,65,78,80,73,78,71,32,67,72,69,78]
    return ''.join(chr(i) for i in Tindex)

def anis():
    l = [65, 110, 105, 115]
    return''.join(chr(i) for i in l)

def gregory():
    letters = [71, 114, 101, 103, 111, 114, 121]
    return ''.join(chr(letter) for letter in letters)
def ronnie(): 
    l = [114,111,110,110,105,101] 
    return ''.join(chr(i) for i in l)

def dereck():
    ascii = [68, 101, 114, 101, 99, 107]
    return ''.join(chr(val) for val in ascii)

#------------------------------------------------------------------------------


# Add your function to the list here
NAME_FUNCTIONS = [james, mario, hasib, jian, anis, gregory, dereck, ronnie]

# Don't edit this
for f in NAME_FUNCTIONS:
    print(f())
