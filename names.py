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

def dereck():
    ascii = [68, 101, 114, 101, 99, 107]
    return ''.join(chr(val) for val in ascii)

def yihui():
    l_e_t_t_e_r_s = [89, 105, 104, 117, 105]
    return ''.join(chr(l_e_t_t_e_r) for l_e_t_t_e_r in l_e_t_t_e_r_s)
#------------------------------------------------------------------------------


# Add your function to the list here
NAME_FUNCTIONS = [james, mario, hasib, jian, anis, gregory, dereck, yihui]


# Don't edit this
for f in NAME_FUNCTIONS:
    print(f())
