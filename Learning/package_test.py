from test_pkg import test1 # Import a module from the package
# "__init__.py" : from test_pkg.test1 import test1_2
from test_pkg import test1_2 # Import a function from a module in the package

test1.test1_1()
test1_2()

from test_pkg import test2 # Import a module from the package

test2.test2_1()
test2.test2_2()

from test_pkg.test3dir import test3 # ------- Import a module from the subpackage
from test_pkg.test3dir.test3 import test3_2 # Import a function from the submodule

test3.test3_1()
test3_2()