import numpy as np
import nltk
#for first time tokenization we need 
# nltk.dowpython nltk_utils.pynload('punkt')

# for steming 
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()


def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
     
     
# a= "Hello, thanks for visiting?"
# print(a)
# a=tokenize(a)
# print(a)   

# words = ["organize", "organizes", "organizing"]
# stemmed_words=[stem(w) for w in words]
# print(stemmed_words)
   


#after tokenization
# sentence = ["hello", "how", "are", "you"]
#after stemming 
# words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
#bags of words
# bog = bag_of_words(sentence,words)
# print(bog)   
    
      
    return bag     