import pytest

from module.classCalc import Calculator

def test_sum():
    # CHECK IF SUM WORKS
    new_calc = Calculator()
    assert new_calc.add(5,8) == 13
def test_subtract():
    # CHECK IF SUBTRACTION WORKS
    new_calc = Calculator()
    assert new_calc.subtract(8,5) == 3
def test_multiply():
    # CHECK IF MULTIPLICATION WORKS
    new_calc = Calculator()
    assert new_calc.multiply(8,5) == 40
def test_divide():
    # CHECK IF DIVISION WORKS
    new_calc = Calculator()
    assert new_calc.divide(10,2) == 5
def test_n_root():
    # CHECK IF ROOT OF N WORKS
    new_calc = Calculator()
    assert new_calc.n_root(8,3) == 2
def test_previous_result():
    # CHECK IF MEMORY WORKS
    new_calc = Calculator()
    new_calc.n_root(8,3) == 2
    assert new_calc.previous_result() != 0
def test_memory_reset():
    # CHECK IF MEMORY RESET WORKS
    new_calc = Calculator()
    new_calc.n_root(8,3) == 2
    new_calc.result_reset()
    assert new_calc.previous_result() == 0
