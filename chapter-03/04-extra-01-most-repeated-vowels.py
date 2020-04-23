"""Write a function, most_repeating_word , that takes a sequence of strings as input. The function should return the string that find the word with the greatest number of repeated vowels. 

That is, if words is set to 

words = ['this', 'is', 'an', 'elementary', 'test', 'example', 'aeiou]

then your function should return 'aeiou' 

""" 

from collections import Counter

def vowel_counter(word):
    count = 0
    for letter in word.lower():
        if letter in 'aeiou':
            count += 1
    return count

def most_repeating_vowels(words):
    return sorted(words,key=vowel_counter, reverse=True)[0]

words = ['this', 'is', 'an', 'elementary', 'test', 'example', 'aeiou']

print (most_repeating_vowels(words))
