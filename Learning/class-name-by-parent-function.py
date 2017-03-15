"""
RESULT: 'self.__class__.__name__' always refers to the name of the present class even if the reference is used in an inherited function
"""

class NameSpeaker(object):
    """ Class that tells you the class name """
    def __init__( self ):
        print self.__class__.__name__
        
class AlsoSprach(NameSpeaker):
    """ We only expect the name to change """
    pass

foo = NameSpeaker() # "NameSpeaker"
bar = AlsoSprach()  # "AlsoSprach"