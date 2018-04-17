import re


def sum_numbers_in_file(filename):
    fh = open(filename)
    running_sum = 0
    for line in fh:
        matches = re.findall('[0-9]+', line)
        if len(matches) == 0: continue
        as_ints = [int(match) for match in matches]
        running_sum = running_sum + sum(as_ints)
    fh.close()
    return running_sum


def one_liner(filename):
    fh = open(filename)
    s = sum([int(match) for match in re.findall('[0-9]+', fh.read())])
    fh.close()
    return s
