"""
Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
"""


class func():
    paragraph = ''
    openParentheses  = tuple('[{(')
    closingParentheses = tuple(')}]')
    parenthesesMap = dict(zip(openParentheses , closingParentheses ))


    def __init__(self , para = ''):
        self.paragraph = para
        
    
    def checkingValidation(self):
        stack = []
        letterList = list(self.paragraph)
        
        for letter in letterList:
            if letter in self.openParentheses:
                stack.append(letter)
            
            elif letter in self.closingParentheses:
                if len(stack) > 0 :
                    openPr = stack.pop()

                    if self.parenthesesMap[openPr] == letter:
                        pass
                    
                    else:
                        stack.append(letter)
                        break

        if len(stack) == 0:
            return 'Parentheses are valid !!!'

        else:
            return 'Parenthesis are invalid !!!'

check = func()

check.paragraph = '[hello { this  is () written in} python]' 
print(check.checkingValidation())