

def m_transp(matrix):
    """
    This function transposes the matrix
    >>> m_transp("2, 2, 3")
    Traceback (most recent call last):
    ...
    TypeError: Matrices must be a list!
    >>> m_transp([[1,2], [3,4,5], [6,7,8]])
    Traceback (most recent call last):
    ...
    ValueError: Matrices must be equilateral!
    """
    if not isinstance(matrix, list):
        raise TypeError('Matrices must be a list!')
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            raise ValueError('Matrices must be equilateral!')
        for j in range(i, len(matrix[i])):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        return

def printable(matrix):
    for i in matrix:
        print(i)
    print('-'*10)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)