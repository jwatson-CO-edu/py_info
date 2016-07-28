def lst(*args):
    """ Return a list composed of the arbitrary 'args' """
    return list(args)

def tpl(*args):
    """ Return a tuple composed of the arbitrary 'args' """
    return tuple(args)

print lst(1,2,3,4)
print tpl(1,2,3,4)