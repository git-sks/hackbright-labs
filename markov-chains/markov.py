"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = open(file_path).read()

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    # Dictionary of individual Markov chains
    chains = {}

    # Break the text down into individual words
    words = text_string.split()

    # Go through the words and form chains consisting of the word at the index
    # and the word that follows, excluding the last bigram.
    # Then add it to the chains dictionary
    for index in range(len(words) - 2):
        # Form a chain from the word at index, and the word that follows
        chain = (words[index], words[index + 1])

        # Make the tuple a key in chains, and add the word that follows those
        # two words to the list value.
        chains[chain] = chains.get(chain, [])
        chains[chain].append(words[index + 2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # Get a random key to start off with as the initial link
    link = choice(list(chains.keys()))

    # Add the initial link to the list of words
    words.extend(link)

    # Get a random follow up word, and add it to words list
    follow_up_word = choice(chains[link])

    try:
        # Loop through the append-link maker-follow up word lookup
        # until you hit a KeyError (have reached a link that doesn't exist in
        # chains dictionary)
        while True:
            # Add the follow up word to the words list
            words.append(follow_up_word)

            # Create a new link from the 2nd word of the current link and the
            # follow up word, and overwrite so the current link is the new link
            link = (link[1], follow_up_word)

            # Look up this new link in the dictionary of chains and make
            # the follow up word a random word from the new link's values
            follow_up_word = choice(chains[link])
    except KeyError:
        # Have hit end of possible follow ups, return a string of the words in
        # words list joined together
        return " ".join(words)


# input_path = "green-eggs.txt"
input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
