"""
RESULT: You can unpack a list into a sequence of variables separated by commas without a special operator
"""

foo , bar , baz = [ 1 , 2 , 3 ]
print foo , bar , baz # 1 2 3
[ foo , bar , baz ] = [ 4 , 5 , 6 ]
print foo , bar , baz # 4 5 6

def get_those_nums():
    """ Return a list of numbers """
    return [ 7 , 8 , 9 ]

foo , bar , baz = get_those_nums()
print foo , bar , baz # 7 8 9
[ foo , bar , baz ] = get_those_nums()
print foo , bar , baz # 7 8 9

# Super Unpack!
[ [ foo , bar , baz ] , [ xur , qua , gan ] , [ guh , wij , kli ] ] = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ] ]
print foo , bar , baz , xur , qua , gan , guh , wij , kli # 1 2 3 4 5 6 7 8 9