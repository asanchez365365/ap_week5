# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info="Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(info.rfind('subjective')) #36
#rfind gives the last occurence of the substring
subjective_word= info[36:] #clearer
print(subjective_word) #subjective
# b. Extract every third word.
every_third_word=info.split()[::3]
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_word_positions= info.split()[::-1]
#this reverses the order of words
reversed_word_positions= ''.join(reversed_word_positions)
#this joins them back into a string
print(reversed_word_positions)
from manipulating_words import manipulationwords
manipulationwords()