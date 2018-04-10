def uppercase_file_contents(fname):
    fh = open(fname)
    lines = fh.read()
    fh.close()
    return lines.upper()
