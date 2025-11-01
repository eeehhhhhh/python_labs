def transpose(mat):
    try:    
        if mat == []:
            return []
        
        n = len(mat[0])
        for i in range(len(mat)):
            if len(mat[i]) != n:
                raise ValueError
        
        new_mat = []
        for j in range(len(mat[0])):  
            new_row = []
            for i in range(len(mat)):  
                new_row.append(mat[i][j])
            new_mat.append(new_row)
        
        return new_mat
    except Exception as err:
        return repr(err)   
print('transpose')
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))


def row_sums(mat):
    try:
        if mat == []:
            return []
        
        n = len(mat[0])
        for i in range(len(mat)):
            if len(mat[i]) != n:
                raise ValueError
        
        sums = []
        for i in range(len(mat)):
            s = 0
            for j in range(len(mat[i])):
                s = s + mat[i][j]
            sums.append(s)
        
        return sums
    except Exception as err:
        return repr(err)
print('row_sums')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


def col_sums(mat):
    try:
        if mat == []:
            return []
        
        n = len(mat[0])
        for i in range(len(mat)):
            if len(mat[i]) != n:
                raise ValueError
        
        sums = []
        for j in range(len(mat[0])):  
            s = 0
            for i in range(len(mat)):  
                s = s + mat[i][j]
            sums.append(s)
        
        return sums
    except Exception as err:
        return repr(err)
print('col_sums')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))