def default_list_param_recur( depth , dflt1 = [] , dflt2 = [] ):
    dflt1.append( depth )
    dflt2.append( depth * 2)
    
    if depth > 0:
        default_list_param_recur( depth-1 , dflt1 , dflt2 )
    
    return dflt1 , dflt2

print default_list_param_recur( 5 ) # ([5, 4, 3, 2, 1, 0], [10, 8, 6, 4, 2, 0])