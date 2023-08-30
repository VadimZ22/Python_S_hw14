import pytest

from Matrix import m_transp




def test_type_with_text():
    with pytest.raises(TypeError, match=r'Matrices must be a list!'):
        m_transp('1,2,3,4,5')

def test_value_with_text():
    with pytest.raises(ValueError, match=r'Matrices must be equilateral!'):
        m_transp([[1,2], [3,4,5], [6,7,8]])


if __name__ == '__main__':
    pytest.main(['-v'])