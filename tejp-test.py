import numpy as np
import tensorflow as tf
corpus_raw = 'He is the king . The king is royal . She is the royal  queen '
# convert to lower case
corpus_raw = corpus_raw.lower()


words = []
for word in corpus_raw.split():
    if word != '.':  # because we don't want to treat . as a word
        words.append(word)
words = set(words)  # so that all duplicate words are removed
word2int = {}
int2word = {}
vocab_size = len(words)  # gives the total number of unique words
for i, word in enumerate(words):
    word2int[word] = i
    int2word[i] = word


# raw sentences is a list of sentences.
raw_sentences = corpus_raw.split('.')
sentences = []
for sentence in raw_sentences:
    sentences.append(sentence.split())


data = []
WINDOW_SIZE = 2
for sentence in sentences:
    for word_index, word in enumerate(sentence):
        for nb_word in sentence[max(word_index - WINDOW_SIZE, 0): min(word_index + WINDOW_SIZE, len(sentence)) + 1]:
            if nb_word != word:
                data.append([word, nb_word])

print(data)
