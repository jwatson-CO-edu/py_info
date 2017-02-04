foo = set( [ 1 , 2 , 3 , 4 , 5 ] )
bar =             set( [ 4 , 5 , 6 , 7 , 8 ] )
baz = set( ['dog'] )

print foo.intersection( bar ) , bar.intersection( foo ) , bar.intersection( baz )

foo = set( [ (1,2) , (2,3) , (3,4) , (4,5) , (5,6) ] )
bar =                         set( [ (4,5) , (5,6) , (6,7) , (7,8) , (8,9) ] )
baz = set( ['dog'] )

print foo.intersection( bar ) , bar.intersection( foo ) , bar.intersection( baz )
print len( bar.intersection( baz ) )

"""
set([4, 5])            set([4, 5])            set([])
set([(4, 5), (5, 6)])  set([(5, 6), (4, 5)])  set([])
0
""" # Order isn't guanteed , but that's OK