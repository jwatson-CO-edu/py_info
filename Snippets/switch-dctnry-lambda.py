# Demonstrate using a dictionary to switch between functions after the fashion of switch/case

from math import pow

funcs = {
    1: lambda x,y: x + y,
    2: lambda x,y: x * y,
    3: lambda x,y: pow(x,y)
}

print funcs[1](2,3)
print funcs[2](2,3)
print funcs[3](2,3)