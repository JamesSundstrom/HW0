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

def jimmy():
    letter = [106,105,109,109,121]
    return ''.join(chr(letter) for l in letter)

def gregory():
    letters = [71, 114, 101, 103, 111, 114, 121]
    return ''.join(chr(letter) for letter in letters)

def matthew(): 
    l = [77, 65, 84, 84, 72, 69, 87] 
    res = "" 
    for c in l: 
        res += chr(c) 
    return res

def leonardo():
    vals = [76, 101, 111, 110, 97, 114, 100, 111]
    return "".join(chr(h) for h in vals)

def dan():
    dans_name = ["A", "a", "a", "A", "A", "a", "a", "a", "a", "a", "a"]
    letter_index = [3,0,13, -33, 10, 14, 11, 14, 13, 0, 24]
    for i in range(len(dans_name)):
        dans_name[i] = chr(ord(dans_name[i]) + letter_index[i])

    return "".join(dans_name)

def yihui():
    l_e_t_t_e_r_s = [89, 105, 104, 117, 105]
    return ''.join(chr(l_e_t_t_e_r) for l_e_t_t_e_r in l_e_t_t_e_r_s)

def samuel_hanono(): # Build via ASCII codes 
    return ''.join(map(chr, (83, 97, 109, 117, 101, 108, 32, 72, 97, 110, 111, 110, 111)))
#------------------------------------------------------------------------------


# Add your function to the list here
NAME_FUNCTIONS = [james, mario, hasib, jian, anis, gregory, dereck, ronnie, leonardo, dan, matthew, yihui, samuel_hanono]

# Don't edit this
for f in NAME_FUNCTIONS:
    print(f())
