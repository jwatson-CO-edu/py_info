foo = 0

print 4 - foo if foo > 0 else 0 #     0
print 4 - ( foo if foo > 0 else 0 ) # 4