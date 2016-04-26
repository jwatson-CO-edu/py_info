# -*- coding: utf-8 -*-
import cPickle # potentially much faster than 'pickle'
import os

# Snippet cannot be used as-is, references other code, example only

def uniq_pts_from_stl(STLpath, pklToFile = False):
    """ Return a set of unique points extracted from an STL file and store them as a list, write to file if 'pklToFile' """
    STLdir, STLfile = os.path.split(STLpath)
    # Turn the closed hand STL into a point cloud only for quick collision checking
    handSTLm = STLpath #'simple-hand-closed_m.stl'
    hand_mesh = mesh.Mesh.from_file(handSTLm)
    print "uniq_pts_from_stl: STL model loaded",handSTLm
    # we cannot guarantee that v0 vectors of neighboring facets are not shared. Therefore, we have to iterate through all three
    #arrays of points, collecting the non-repeats into an array
    pointsOnly = []
    # URL, Comparison of uniqueifiers if you need this done faster: http://www.peterbe.com/plog/uniqifiers-benchmark
    for vList in [hand_mesh.v0 , hand_mesh.v1 , hand_mesh.v2]: # for each collection of points
        for point in vList: # for each point in the collection, check if the point is equal to any in the list of unique points
            if not eq_in_list(point, pointsOnly, eq_vec): # This is safe to do b/c iteration ends before the list is modified
                pointsOnly.append(point) # The point is unique, add it to the unique list
    
    print "Collected",len(pointsOnly),"unique points."
    
    if pklToFile: # Set to true to save the hand points
        pklPath = 'output/' + STLfile[:-4] + '.pkl'
        f = open( pklPath , 'wb') # open a file for binary writing to receive pickled data
        cPickle.dump(pointsOnly, f) # changed: pickle.dump --> cPickle.dump
        f.close()
        print "STL was cPickled to as a list of R3 points to file:", pklPath
        
    return pointsOnly

def load_pkl_struct(pklFilePath):
    """ Load a pickled object and return it, return None if error """
    fileLoaded = False
    rtnStruct = None
    try:
        f = open( pklFilePath , 'rb')
        fileLoaded = True
    except Exception as err:
        print "load_pkl_struct: Could not open file,",pklFilePath,",",err
    if fileLoaded:
        try:
            rtnStruct = cPickle.load(f)
        except Exception as err:
            print "load_pkl_struct: Could not unpickle file,",pklFilePath,",",err
        f.close()
    return rtnStruct