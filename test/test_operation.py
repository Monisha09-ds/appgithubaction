from src.math_operation import add,power

def test_add():
    assert add(2,3)==5
    assert add(-2,+2)==0

def test_power():
    assert power(0,4)==1
    assert power(1,0)==0
    assert power(2,3)==9