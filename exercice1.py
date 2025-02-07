def addToEach(n, lst):
    return [x + n for x in lst]


print(addToEach(3, [1, 2, 3, 4]))  


def removeDuplicates(lst):
    return list(set(lst))  


print(removeDuplicates([1, 2, 2, 3, 4, 4, 5]))  
