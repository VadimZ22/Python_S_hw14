

def check_triangle(a, b, c):
    """
    The function checks the possibility of creating a triangle with sides
    a, b, c, as well as the type of triangle in case of creation.
    >>> check_triangle(2, 2, '3')
    Traceback (most recent call last):
    ...
    TypeError: The numbers a,b,c must be an integer or float type
    >>> check_triangle(-2, 2, 3)
    Traceback (most recent call last):
    ...
    ValueError: The numbers a,b,c must be grater then 0
    >>> check_triangle(2, 3, 9)
    Traceback (most recent call last):
    ...
    ValueError: One side of a triangle cannot be greater than the other two
    >>> check_triangle(3, 3, 3)
    'Triangle is equilateral'
    >>> check_triangle(3, 3, 5)
    'Triangle isosceles'
    >>> check_triangle(3, 4, 5)
    'scalene triangle'
    """

    if not isinstance(a, int|float) or not isinstance(b, int|float) or not isinstance(c, int|float):
        raise TypeError('The numbers a,b,c must be an integer or float type')
    elif a <= 0 or b <= 0 or c <= 0:
        raise ValueError('The numbers a,b,c must be grater then 0')
    elif a > (b + c) or b > (a + c) or c > (a + b):
        raise ValueError('One side of a triangle cannot be greater than the other two')
    else:
        if (a == b) or (a == c) or (b == c):
            if (a == b == c):
                return 'Triangle is equilateral'
            else: return 'Triangle isosceles'
        else: return 'scalene triangle'

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)