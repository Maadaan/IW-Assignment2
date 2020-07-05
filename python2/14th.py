"""
Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]
"""

import csv

def func(files):
    resultData = []
    with open(files , newline='') as file:
        fileRead = csv.reader(file , delimiter = ',')
        isFirstRow = True

        for data in fileRead:
            tmp = {}

            if isFirstRow:
                keys = data
                isFirstRow = False
                continue

            for i in range(len(keys)):
                tmp[keys[i]] = data[i]
            
            resultData.append(tmp)    
    file.close()
    return resultData

print(func('file13.csv'))