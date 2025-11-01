def min_max(nums):
    try:
        if nums == []:
            raise ValueError
        
        minimum = nums[0]
        maximum = nums[0]

        for i in range(len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]
            if nums[i] > maximum:
                maximum = nums[i]

        return (minimum, maximum)
    except Exception as err:
        return repr(err)
print('min_max')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums):
    if nums == []:
        return []
    
    unique = []
    for x in nums:
        if x not in unique:
            unique.append(x)

    n = len(unique)
    for i in range(n):
        for j in range(0, n-i-1):
            if unique[j] > unique[j+1]:
                unique[j], unique[j+1] = unique[j+1], unique[j]
    
    return unique

print('unique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat):
    try:
        result = []
        for i in range(len(mat)):
            if type(mat[i]) != list and type(mat[i]) != tuple:
                raise ValueError
            
            for j in range(len(mat[i])):
                result.append(mat[i][j])
        
        return result
    except Exception as err:
        return repr(err)
print('flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))