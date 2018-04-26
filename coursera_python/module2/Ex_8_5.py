def count_from_lines(file):
    count = 0
    fh = open(file)
    for line in fh:
        s = line.strip()
        if "From " in s:
            count = count + 1
            words = s.split()
            print( words[1] )
    return count
