import numpy as np

def num_range_to_bins( pMin , pMax , numBins ):
    """ Return the bounds to 'numBins' bins between 'pMin' and 'pMax' """
    partitions = [ float(item) for item in np.linspace( pMin , pMax , numBins + 1 ) ] # Get the bounds of the bins
    return [ ( partitions[ pDex ] , partitions[ pDex + 1 ] ) for pDex in xrange( len( partitions ) - 1 ) ]  # Translate bins to 2-tuples

def bindex( bins , num ):
    """ Return the index of the bin in 'bins' to which 'num' belongs , 'bins' constructed according to 'num_range_to_bins' """
    for bDex , bounds in enumerate( bins ):
        if num <= bounds[1]:
            return bDex
    return None

bins = num_range_to_bins( 2, 15 , 25 )
for b in bins:
    print b[1] - b[0] ,
print 
print bins

print bindex( bins , 5 ) # 5 # Correct
    