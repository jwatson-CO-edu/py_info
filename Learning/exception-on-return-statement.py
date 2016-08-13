def converter( inputStr ):
    try:
        return int(inputStr)/0 # What will happen if there is an exception when returning
    except ZeroDivisionError:
        pass
    return inputStr

print converter(4) # 4 , Error as usual - order of ops means that the error happens before return