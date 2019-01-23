import sys

def matrix_chain(mat, i, j):
    '''
        Calculate the amount of multiplcations you'd need to make given
        a list of matrix sizes

        Arguments:
            :mat: The list of matrix sizes
            :i: the starting point within the matrix
            :j: the ending point within the matrix
    '''
    if i == j:
        return 0
    minimum_computations = sys.maxsize
    for k in range(i, j):
        count = (matrix_chain(mat, i, k) + matrix_chain(mat, k + 1, j) + mat[i - 1] * mat[k] * mat[j])

        if count < minimum_computations:
            minimum_computations = count;
    return minimum_computations

matrix_sizes = [20, 30, 45, 50]
print('minimum multiplications are', matrix_chain(matrix_sizes, 1, len(matrix_sizes) - 1 ))
