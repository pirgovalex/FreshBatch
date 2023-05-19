with open("cats.txt") as f:
    content = f.read()
    # split the contents into words
    words = content.split()
    # create an empty dictionary
    word_counts = {}
    # loop through the words and add them to the dictionary
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # sort the dictionary by frequency
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    # get the top 10 most used words
    top_10_words = sorted_word_counts[:15]
    # print the top 10 most used words
    for word, count in top_10_words:
        print(f"{word}: {count}")
