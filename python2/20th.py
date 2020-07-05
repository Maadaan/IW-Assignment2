"""
Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""





class findingElements:

    def __init__(self, inp_arr=None):
        if inp_arr is None:
            inp_arr = []
        self.inp_arr = inp_arr

    def func(self):
        resultList = []
        iter_dur = len(self.inp_arr)
        for fst_index in range(iter_dur):
            for sec_index in range(iter_dur):
                if sec_index != fst_index:
                    for third_index in range(iter_dur):
                        if (third_index != sec_index
                                and third_index != sec_index):
                            if (self.inp_arr[fst_index]
                                    + self.inp_arr[sec_index]
                                    + self.inp_arr[third_index] == 0):
                                resultList.append([self.inp_arr[fst_index],
                                                   self.inp_arr[sec_index],
                                                   self.inp_arr[third_index]])
        for item in resultList:
            item.sort()
        no_duplicates = set(tuple(x) for x in resultList)
        resultList = [list(lst) for lst in no_duplicates]
        return resultList


element = findingElements([-25, -10, -7, -3, 2, 4, 8, 10, 17])
print(element.func())

