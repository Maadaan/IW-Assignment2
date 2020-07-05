"""
Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""

# words = 'level'
words = 'levels'
words = 'level'


def func(word):
    reversedWords = word[::-1]

    if word == reversedWords:
        print('The word {} is palindrome .' .format(word))
    
    else:
        print('The word {} is not in palindrome .' .format(word))

func(words)