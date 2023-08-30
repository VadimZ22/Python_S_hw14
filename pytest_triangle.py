import pytest

from Triangle import check_triangle



def test_type():
    with pytest.raises(TypeError):
        check_triangle(2, 4, '3.5')

def test_value():
    with pytest.raises(ValueError):
        check_triangle(-2, 2, 3)
        check_triangle(2, 3, 9)

def test_type_with_text():
    with pytest.raises(TypeError, match=r'The numbers a,b,c must be an integer or float type'):
        check_triangle(2, 2, '3')

def test_value_with_text():
    with pytest.raises(ValueError, match=r'One side of a triangle cannot be greater than the other two'):
        check_triangle(2, 2, 10)


if __name__ == '__main__':
    pytest.main(['-v'])