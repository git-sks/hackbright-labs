# put your code here.
import sys

def print_word_count():
    """Print the number of times each word in a file occurs in said file."""

    # word_file = open('test.txt')
    # word_file = open('twain.txt')
    try:
        word_file = open(sys.argv[1])

        word_counts = {}

        for line in word_file:
            # Go through each line, splitting it into its individual words
            line = line.rstrip()
            words = line.split()

            # For each word occurance in a line, increment its count
            for word in words:
                word = word.strip("'\".,?!*;:_-)(}{")
                word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1

        # Print each unique word and its number of occurances
        for unique_word, count in word_counts.items():
            print(f"{unique_word} {count}")
    except IndexError:
        print("Please include a file to run the program on.")

# Testing
print_word_count()