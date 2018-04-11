def get_sorted_unique_word_list(file):
    unique_words = list()
    fh = open(file)
    for line in fh:
        words = line.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    unique_words.sort()
    fh.close()
    return unique_words


def count_from_lines(file):
    count = 0
    fh = open(file)
    for line in fh:
        s = line.strip()
        if "From " in s:
            count = count + 1
            l = s.split()
            print(l[1])
    return count
