import nltk

# from nltk.org/book.ch02.html
# testing functions

def lexical_diversity(text_data):
    word_ct = len(text_data)
    vocab_sz = len(set(text_data))
    diversity_score = vocab_sz / word_ct
    return diversity_score

from nltk.corpus import genesis
kjv = genesis.words("english-kjv.txt")
print(lexical_diversity(kjv))

def plural(word):
    if word.endswith("y"):
        return word[:-1] + "ies"
    elif word[-1] in "sx" or word[-2:] in ["sh", "ch"]:
        return word + "es"
    else:
        return word + "s"

print(plural("cat"))
print(plural("fish"))

#finding unusual or misspelled words
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

#words in Jane Austen's Sense and Sensibility
print(unusual_words(nltk.corpus.gutenberg.words("austen-sense.txt")))

#STOPWORDS occur in high frequency and add minimal lexical content
#ftn to determine percent of non-stopwords in a text
def not_stopwords(text):
    stopwords = nltk.corpus.stopwords.words("english")
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

print(not_stopwords(nltk.corpus.gutenberg.words("austen-sense.txt")))