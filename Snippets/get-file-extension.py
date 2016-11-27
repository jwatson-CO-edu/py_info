def get_ext( fName ): # NOTE: everything after the last '.' is assumed to be the extension
    """ Return the file extension of a file, including the '.' , otherwise return an empty string if there is no '.' """
    if '.' in fName: 
        ext = ""
        i = -1
        while( fName[i] != '.' ):
            ext = fName[i] + ext
            i -= 1
        return "." + ext
    else:
        return ''
    
print get_ext( "fName.py" ) #  ".py"
print get_ext( "fName.txt" ) # ".txt"
print get_ext( "fName.100" ) # ".100"
print get_ext( "fName." ) #    "."
print get_ext( "." ) #         "."
print get_ext( "fName" ) #     ""