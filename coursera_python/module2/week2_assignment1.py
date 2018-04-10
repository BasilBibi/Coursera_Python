def print_file_contents(fname):
    fh = open(fname)
    for i in fh :
        print( i.rstrip().upper() )
