zeros = [ [0,0,0] , 
          [0,0,0] , 
          [0,0,0] ]

print zeros

for rDex , row in enumerate( zeros ): # Operate on the list as we go
    row[rDex] = 1
    
print zeros

"""
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
"""