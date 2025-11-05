# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic= 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find('c'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet= 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7:10])
#print(hij_index)
# b. Extract every second letter starting from 'a' to 'm'.
every_second_letter = alphabet [0:13:2]
# c. Reverse the entire string using slicing.
reversed_alphabet = alphabet[::-1] # <--- reverse a string
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote=  "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find('John F. Kennedy'))
personality_name = quote[78:] #cleaner
print(personality_name) #John F Kennedy

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

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
mottos= ["make","haste", "slowly."]
separator=""
result_string= 
print(result_string)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
text= "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
ltetter_to_count='i'
count=phrase.count(letter_to_count)
