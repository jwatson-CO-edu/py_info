# -*- coding: utf-8 -*-
# URL, 'namedtuple' as a handy stand-in for a c-struct, http://www.blog.pythonlibrary.org/2016/03/15/python-201-namedtuple/
from collections import namedtuple
 
Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine',
                   cost=1200.00, amount=10)
print auto_parts.id_num