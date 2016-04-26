# ud-module-test.py
# James Watson, 2015 August
# Load a user defined module and see what is available

import trialModule

print(trialModule.foo) # prints "1"
print(trialModule.bar) # prints "2"
print(trialModule.baz) # prints "3"

print( trialModule.var_sum() ) # prints "6"

# Conclusion: Both defined variables and functions are avaialable in the module namespace once the module is loaded
