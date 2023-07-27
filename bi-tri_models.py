#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.corpus import brown
from nltk.tokenize import word_tokenize

import nltk
nltk.download('brown')
# Loading the corpus
corpus = brown.words()

# Case folding and getting vocab
lower_case_corpus = [w.lower() for w in corpus]
vocab = set(lower_case_corpus)

print('CORPUS EXAMPLE: ' + str(lower_case_corpus[:30]) + '\n\n')
print('VOCAB EXAMPLE: ' + str(list(vocab)[:10]))

print('Total words in Corpus: ' + str(len(lower_case_corpus)))
print('Vocab of the Corpus: ' + str(len(vocab)))

bigram_counts = {}
trigram_counts = {}

# Sliding through corpus to get bigram and trigram counts
for i in range(len(lower_case_corpus) - 2):
    # Getting bigram and trigram at each slide
    bigram = (lower_case_corpus[i], lower_case_corpus[i+1])
    trigram = (lower_case_corpus[i], lower_case_corpus[i+1], lower_case_corpus[i+2])
    
    # Keeping track of the bigram counts
    if bigram in bigram_counts.keys():
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1
    
    # Keeping track of trigram counts
    if trigram in trigram_counts.keys():
        trigram_counts[trigram] += 1
    else:
        trigram_counts[trigram] = 1

print("Example, count for trigram ('the', 'king','of') is: " + str(trigram_counts[('the', 'king','of')]))

# Function takes sentence as input and suggests possible words that comes after the sentence  
def suggest_next_word(input_, bigram_counts, trigram_counts, vocab):
    # Consider the last bigram of sentence to predict next word
    tokenized_input = word_tokenize(input_.lower())
    last_bigram = tokenized_input[-2:] #last two words

    
    # Calculating probability for each word in vocab
    vocab_probabilities = {} #defining dictionary for word as key and its probability of occurence as value
    for vocab_word in vocab:
        test_trigram = (last_bigram[0], last_bigram[1], vocab_word) #last two words and one word from vocab
        test_bigram = (last_bigram[0], last_bigram[1]) #last two words

        test_trigram_count = trigram_counts.get(test_trigram, 0) #access the count of test trigram from trigram_counts which was declared earlier
        test_bigram_count = bigram_counts.get(test_bigram, 0)
        
        probability = test_trigram_count / test_bigram_count #using formula P(w2/w1) = count(w2,w1)/count(w1)
        vocab_probabilities[vocab_word] = probability #loading the calculated value using dict[key]=value for that key which is stored in probability

    # Sorting the vocab probability in descending order to get top probable words (top 3)
    top_suggestions = sorted(vocab_probabilities.items(), key=lambda x: x[1], reverse=True)[:3] 
    return top_suggestions

import nltk
nltk.download('punkt')
suggest_next_word('I am the king', bigram_counts, trigram_counts, vocab)


suggest_next_word('I am the', bigram_counts, trigram_counts, vocab)

suggest_next_word('I am the king of france', bigram_counts, trigram_counts, vocab)


suggest_next_word('I am the king of france and', bigram_counts, trigram_counts, vocab)


# In[ ]:





# In[ ]:




