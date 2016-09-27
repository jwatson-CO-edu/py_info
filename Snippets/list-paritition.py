from math import floor

nums = range(100)
print nums
N = 6
div = int( floor( 100 / (N+1) ))
print div

groups = []
for i in xrange(N):
    if i < N-1:
        groups.append( nums[i*div:(i+1)*div] )
    else:
        groups.append( nums[(i+1)*div:] )
        
for group in groups:
    print group , len(group)