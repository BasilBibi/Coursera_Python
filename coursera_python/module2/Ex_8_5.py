def count_from_lines(file):
    count = 0
    fh = open(file)
    for line in fh:
        s = line.strip()
        if "From " in s:
            count = count + 1
    fh.close()
    return count
