from lib2to3.pgen2.literals import test
import numpy as np


def distinct_words(corpus):
    """ Determine a list of distinct words for the corpus.
        Params:
            corpus (list of list of strings): corpus of documents
        Return:
            corpus_words (list of strings): sorted list of distinct words across the corpus
            num_corpus_words (integer): number of distinct words across the corpus
    """
    corpus_words = []
    num_corpus_words = -1

    # ------------------
    # Write your implementation here.
    flatten_corpus = [y for x in corpus for y in x]
    corpus_words = sorted(set(flatten_corpus))
    num_corpus_words = len(corpus_words)
    # ------------------

    return corpus_words, num_corpus_words


def compute_co_occurrence_matrix(corpus, window_size=4):
    """ Compute co-occurrence matrix for the given corpus and window_size (default of 4).

        Note: Each word in a document should be at the center of a window. Words near edges will have a smaller
              number of co-occurring words.

              For example, if we take the document "<START> All that glitters is not gold <END>" with window size of 4,
              "All" will co-occur with "<START>", "that", "glitters", "is", and "not".

        Params:
            corpus (list of list of strings): corpus of documents
            window_size (int): size of context window
        Return:
            M (a symmetric numpy matrix of shape (number of unique words in the corpus , number of unique words in the corpus)): 
                Co-occurence matrix of word counts. 
                The ordering of the words in the rows/columns should be the same as the ordering of the words given by the distinct_words function.
            word2ind (dict): dictionary that maps word to index (i.e. row/column number) for matrix M.
    """
    words, num_words = distinct_words(corpus)
    M = None
    word2ind = {}

    # ------------------
    # Write your implementation here.
    M = np.zeros((num_words, num_words))

    for i, word in enumerate(words):
        word2ind[word] = i

    for sentence in corpus:
        print(sentence)
        length = len(sentence)
        # print(length)
        for index, word in enumerate(sentence):
            # print(index, word)
            words_in_window = list()

            if index < window_size:
                for i in range(0, index):
                    words_in_window.append(sentence[i])
            else:
                for i in range(index-window_size,index):
                    words_in_window.append(sentence[i])

            if length-index <= window_size:
                for i in range(index+1, length):
                    words_in_window.append(sentence[i])
            else:
                for i in range(index+1,index+window_size+1):
                    words_in_window.append(sentence[i])

            # print('words_in_window', words_in_window)

            for w in words_in_window:
                M[word2ind[word]][word2ind[w]] += 1
                # print(word2ind[word], word2ind[w])
                # print(word, w)
            # print('='*20)
        # ------------------

    return M, word2ind


START_TOKEN = '<START>'
END_TOKEN = '<END>'
test_corpus = ["{} All that glitters isn't gold {}".format(START_TOKEN, END_TOKEN).split(
    " "), "{} All's well that ends well {}".format(START_TOKEN, END_TOKEN).split(" ")]

# for i in range(1,5):
#     print(i)
# print(test_corpus)

M,word2ind=compute_co_occurrence_matrix(test_corpus, 1)

print(word2ind)

print(M)