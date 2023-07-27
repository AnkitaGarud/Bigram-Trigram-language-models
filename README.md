# Bigram-Trigram-language-models
The provided code is a Python script that demonstrates the process of creating and utilizing bigram and trigram language models based on the "brown" corpus from the NLTK library. The code aims to suggest possible words that come after a given input sentence using these language models. 

code explained step by step:
Importing necessary libraries and downloading the "brown" corpus and tokenization resources from NLTK.
Loading the "brown" corpus and converting it to lowercase to ensure consistency.
Building a vocabulary set to keep track of unique words in the corpus.
Creating dictionaries to store the counts of bigrams and trigrams in the corpus.
Iterating through the lowercased corpus to calculate the occurrences of each bigram and trigram.
Defining a function named "suggest_next_word" that takes an input sentence, bigram counts, trigram counts, and the vocabulary as parameters.
Inside the function, tokenizing the input sentence and considering the last two words (last bigram) to predict the next word.
Calculating the probability of each word in the vocabulary following the last bigram using the formula P(w2|w1) = count(w1, w2) / count(w1).
Sorting the vocabulary probabilities in descending order to get the top three most probable words.
The code includes four function calls to the "suggest_next_word" function with different input sentences to demonstrate the word suggestions for each.
