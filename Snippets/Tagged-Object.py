# -*- coding: utf-8 -*-

def sep(title = ""):
    print "=======" + ' ' + title + ' ' + "======="

# ~~~ Rev 2 ~~~

class TaggedObject(object):
    
    def __init__(self):
        """ The simplest means to give each object a unique tag """ # NOTE: No need for a global lookup at this time
        self.tag = self.__class__.__name__ + str(id(self))
        print self.tag
        
class foo(TaggedObject):
    pass

bar = [ TaggedObject() for i in xrange(10) ]
baz = [ foo() for i in xrange(10) ]

# ~~~ Rev 1 ~~~

# == Tagged Base Class ==
def Tagged_init(cls, pTypName = 'DEFAULT'):
    """ Used to init 'TaggedObject' and its subclasses """ 
    # It seems important that this be called outside of the any class declaration because if a subclass of 'TaggedObject'
    #or any of its subclasses is declared after instances of a parent class have been created, a call to 'super' should 
    #not reset the counter of a class that already has instances. This function was created to more or less guarantee 
    #that every instance has its own unique tag.
    cls.typName = pTypName
    cls.totalInstance = 0

class TaggedObject(object):
    typName = "TaggedObject"
    totalInstance = 0
        
    def genTag(self):
        """ Increment the tally of instances of this object and generate a tag for this instance """
        self.__class__.totalInstance += 1
        self.tag = self.typName + '_' + str(self.__class__.totalInstance)
        
    def __init__(self):
        """ Generate tag """
        self.genTag()
        self.alias = None # Default alias is 'None'
        
    def give_alias(self, nick):
        """ Assign alias, must be hashable """
        if isinstance(nick, collections.Hashable):
            self.alias = nick
        else:
            raise ValueError( "TaggedObject.give_alias: Alias must be hashable, received unhashable object" + str(nick) )
   
# = class TaggedLookup =
     
class TaggedLookup(object):
    """ A container for TaggedObjects, can be used for lookup and removal by tag and alias """
    
    def __init__(self):
        self.lookupByTag = {} # Dictionary of objects stored by tag
        self.lookupByAls = {} # Dictionary of objects stored by alias
        self.verbose = False
        
    def get_by_tag(self, pTag):
        """ Return an object reference from the lookup with a matching tag if it exists, otherwise return None """
        rtnObj = None
        try:
            rtnObj = self.lookupByTag[pTag]
        except KeyError:
            if self.verbose:
                print "Object with tag",pTag,"DNE in this problem"
        return rtnObj
        
    def get_by_als(self, pAls):
        """ Return an object reference from the lookup with a matching alias if it exists, otherwise return None """
        rtnObj = None
        try:
            rtnObj = self.lookupByAls[pAls]
        except KeyError:
            if self.verbose:
                print "Object with alias",pAls,"DNE in this problem"
        return rtnObj
        
    def iterTag(self):
        """ Return an iterator for the tag dictionary """
        return self.lookupByTag.iteritems()
        
    def iterAls(self):
        """ Return an iterator for the alias dictionary """
        return self.lookupByAls.iteritems()
        
    def item_list(self):
        """ Return a list of all items (values) in the lookup """
        return self.lookupByTag.values()
        
    def add_objs(self, *pObjs):
        """ Add all TaggedObjects in 'pObjs' and add references to tag and alias lookups """
        for obj in pObjs:
            if self.verbose: # Is this really necessary?
                print obj
            if obj.tag in self.lookupByTag: # Reject if tag exists in Agent lookup
                print "An object with tag",obj.tag,"already exists in the problem"
            else: # else Agent with this tag has not been added, add it to the tag lookup
                self.lookupByTag[obj.tag] = obj
                if obj.alias: # Store a reference in the alias lookup, this will overwrite a reference previously stored
                    self.lookupByAls[obj.alias] = obj # If there is an alias collision, old will be overwritten!
                    
    def rm_by_tag(self, pTag):
        """ Pop an object with tag matching 'pTag' from all lookups, if it is found in lookups """
        rtnObj = None
        try:
            ref = self.lookupByTag[pTag]
            rtnObj = self.lookupByTag.pop(pTag)
            if ref.alias:
                self.lookupByAls.pop(ref.alias)
        except KeyError:
            print "Object with tag",pTag,"DNE in this problem"
        return rtnObj
            
    def rm_by_als(self, pAls):
        """ Pop an object with alias matching 'aAls' from all lookups, if it is found in lookups """
        rtnObj = None
        try:
            ref = self.lookupByAls[pAls]
            rtnObj = self.lookupByAls.pop(pAls)
            self.lookupByTag.pop(ref.tag)
        except KeyError:
            print "Object with alias",pAls,"DNE in this problem"
        return rtnObj
            
    def rm_by_ref(self, obj):
        """ Pop the object that 'obj' references """
        return self.rm_by_tag(obj.tag)
        
    def __len__(self):
        """ Return the number of objects held in the lookup """
        # NOTE: This function assumes that the tag lookup holds the complete list of objects, per design
        return len(self.lookupByTag) # Return the length of the tag dictionary
        
    def __str__(self):
        """ Print all contents by tag """
        rtnStr = ''
        for key, val in self.lookupByTag.iteritems():
            rtnStr += str(key) + '\t\t' + str(val) + endl # depends on 'ResearchEnv'
        return rtnStr

# = End TaggedLookup =    

# ~~~ Rev 0 ~~~

class TaggedObject(object):
    objName = "TaggedObject"
    totalInstance = 0
    def genTag(self):
        self.__class__.totalInstance += 1
        self.tag = self.objName + '_' + str(self.__class__.totalInstance)
    def __init__(self):
        self.genTag()

class Node(TaggedObject):
    # Note that __init__ is inherited from the parent class if it is not defined
    objName = "Node"   # 
    totalInstance = 0
    
foo = TaggedObject()
print foo.tag
bar = Node()
print bar.tag
baz = TaggedObject()
qux = TaggedObject()
sep('Object Collection')
print foo.tag # same TaggedObject as above
print bar.tag # same Node as above
print baz.tag # new TaggedObject
print qux.tag # new TaggedObject