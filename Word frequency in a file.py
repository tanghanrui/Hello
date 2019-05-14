# Date: 7/18/2018
# Author: Hanrui Tang
# This small project analyzes the word frequency in a test file

# wordfreq.py
# use main function because when this program is included in other programs, I don't want them to be executed right away

def byFreq(pair):
    return pair[1]

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the most frequent words.\n")

    # get the sequence of n words from the file
    fname = input("File to analyze: ")
    text = open(fname, 'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':   # remove unnecessary characters
        text = text.replace(ch, ' ')
    words = text.split()                            # get a list of word spliced by space(by default)

    # Create a list for stop words
    stop_words = ["a", "an", "and", "as", "at", "be", "but", "etc", "for", "in", "it", "its", "is", "of", "or",
                  "so", "such", "the", "this", "to", "with"]

    # get positive and negative words
    # ignore the first 35 lines
    neg_words = open("negative-words.txt", "r", encoding="utf-8", errors="ignore").read().splitlines()[35:]

    pos_words = open("positive-words.txt", "r", encoding="utf-8", errors="ignore").read().splitlines()[35:]

    # construct dictionaries of word counts
    counts = {}
    counts_positive = {}
    counts_negative = {}

    for w in words:
        if w not in stop_words:                     # remove stop words from words count
            counts[w] = counts.get(w, 0) + 1
        if w in pos_words:
            counts_positive[w] = counts_positive.get(w, 0) + 1
        if w in neg_words:
            counts_negative[w] = counts_negative.get(w, 0) + 1

    # define a function to return words frequency
    def frequency(count_frequency, num):
        items = list(count_frequency.items())
        items.sort(key=byFreq, reverse=True)
        for i in range(num):
            word, count = items[i]
            print("{0:<15}{1:>5}".format(word, count))

    # output analysis of n most frequent words.
    n = int(input("Output analysis of how many words? "))
    frequency(counts, n)
    print("\n")

    # output analysis of top 5 positive words.
    print("Top 5 positive words")
    frequency(counts_positive, 5)
    print("\n")

    # output analysis of top 5 negative words.
    print("Top 5 negative words")
    frequency(counts_negative, 5)
    print("\n")

    # define a function to calculate sentiment score
    def sentiment_score(positive, negative):
        positive_score = 0
        negative_score = 0
        for value in positive.values():
            positive_score += int(value)
        for value in negative.values():
            negative_score += int(value)
        print(positive_score - negative_score)

    # print out sentiment score
    print("Teacher's sentiment score:")
    sentiment_score(counts_positive, counts_negative)

if __name__ == '__main__':  main()
