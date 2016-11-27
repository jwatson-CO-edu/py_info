# Get all the lines , then write all the lines

f = open( 'testFile.txt' , 'r' )
lines = f.readlines() # The entire file now exists in RAM, this is probably OK
f.close()
f = open( 'outFile1.txt' , 'w' )
f.writelines( lines ) # Note that this does not add extra newlines
f.close()

# Get and write at the same time

with open( 'testFile.txt' , 'r') as infile:
    with open( 'outFile2.txt' , 'w' ) as outfile:
        for line in infile: # Using this method, only one line of the file is ever in memory
            outfile.write( line ) # Here also, no extra newlines are added