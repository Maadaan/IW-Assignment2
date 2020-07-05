"""
Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.
"""



def func(x):
    final = ''
    for item in x:
        if item.isupper():
            final += '_'+item.lower()
        else:
            final += item
    
    if final[0] == "_":
        final = final[1:]
    return final

print(func('ThisIsCamelCase'))
