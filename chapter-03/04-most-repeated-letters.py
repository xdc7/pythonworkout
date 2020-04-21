"""Write a function, most_repeating_word , that takes a sequence of strings as input. The function should return the string that contains the greatest number of repeated letters. In other words: for each word, find the letter that appears the most times find the word whose most-repeated letter appears more than any other


That is, if words is set to 

words = ['this', 'is', 'an', 'elementary', 'test', 'example']

then your function should return 'elementary' . 

That’s because: this has no repeating letters is has no repeating letters an has no repeating letters elementary has one repeating letter, e , which appears three times test has one repeating letter, t , which appears twice example has one repeating letter, e , which appears twice So the most common letter in elementary appears more often than the most-common letters in any of the other words. (If it’s a tie, then any of the appropriate words can be returned.) You will probably want to use Counter , from the collections module, which is perfect for counting the number of items in a sequence. More information is here: docs.python.org/3/library/collections.html#collections.Counter Pay particular attention to the most_common method ( docs.python.org/3/library/collections.html?#collections.Counter.most_common ), which will come in handy here.

""" 

from collections import Counter

def most_repeating_word(words):
    result = words[0]
    mostRepeating = Counter(words[0]).most_common(1)[0][1]
    for word in words:
        c = Counter(word).most_common(1)[0][1]
        if c > mostRepeating:
            mostRepeating = c
            result = word
    return result




words = ['this', 'is', 'an', 'elementary', 'test', 'example']

print (most_repeating_word(words))