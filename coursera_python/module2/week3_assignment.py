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
