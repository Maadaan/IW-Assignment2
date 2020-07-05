"""
3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
"""


def func(word1 , word2):
    
    list1 = list(word1)
    list1.sort()

    list2 = list(word2)
    list2.sort()

    return(list1 == list2)

print(func('listen', 'silent'))

print(func('cat', 'rat'))




