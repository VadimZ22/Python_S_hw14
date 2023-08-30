

def m_transp(matrix):
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