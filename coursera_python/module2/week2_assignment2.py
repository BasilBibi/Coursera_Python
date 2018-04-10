def calc_avg_spam_confidence(fname):
    fh = open(fname)
    running_total = 0
    count = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"): continue
        running_total = running_total + float(line[line.find("0"):])
        count = count + 1
    return running_total / count
