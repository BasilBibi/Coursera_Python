'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the
sent the greatest number of mail messages. The program looks for 'From ' lines and
takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count
of the number of times they appear in the file. After the dictionary is produced, the
program reads through the dictionary using a maximum loop to find the most prolific committer.
'''


def get_most_sender(file):
    fh = open(file)
    hist = dict()
    for line in fh:
        if "From " not in line: continue
        words = line.split()
        emailaddr = words[1]
        hist[emailaddr] = hist.get(emailaddr, 0)+1
    fh.close()
    #return get_max_value_from_hist(hist)
    #return get_max_value_from_hist_fp(hist)
    return get_mv_list_comprehension(hist)


def get_max_value_from_hist(hist):
    dict_totals = dict()
    for k, v in hist.items():
        dict_totals[v] = k
    m = max(dict_totals.keys())
    addr = dict_totals[m]
    return addr + " " + str(m)


def get_max_value_from_hist_fp(hist):
    def f(kv): return kv[1], kv[0]
    x = map(lambda kv: f(kv), hist.items())
    a = list(x)
    m = max(a)
    return m[1] + " " + str(m[0])


def get_max_value_from_hist_anon_lambda(hist):
    x = map(lambda kv: (kv[1], kv[0]), hist.items())
    a = list(x)
    m = max(a)
    return m[1] + " " + str(m[0])


def get_mv_list_comprehension(hist):
    a = [(t[1], t[0]) for t in hist.items()]
    m = max(a)
    return m[1] + " " + str(m[0])
