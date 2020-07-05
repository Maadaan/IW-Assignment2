"""
Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""

def func(nums):
    if nums > 3:
        for i in range(2,nums):
            if nums % i == 0:
                return False
            else:
                return True
    
    elif nums >= 0:
        return True
    
    else:
        raise ValueError('Please enter a valid number : ')

print(func(nums = 10))
print(func(nums = 9))
