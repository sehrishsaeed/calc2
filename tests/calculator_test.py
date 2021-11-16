"""Testing the Calculator"""
# pylint: disable=unused-argument
# pylint: disable=redefined-outer-name
# pylint: disable=expression-not-assigned
import pprint
import pytest
from calculator.calculator import Calculator


@pytest.fixture
def clear_history():
    """ clears history after each run """
    Calculator.empty_history()


def test_calculator_add(clear_history):
    """ tests the addition between 2 numbers """
    assert Calculator.add_number(5, 5) == 10
    assert Calculator.add_number(25, 25) == 50
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(5, -5) == 0
    assert Calculator.history_count() == 4
    assert Calculator.last_calc_to_history() == 0
    pprint.pprint(Calculator.history)


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(10, 5) == 5


def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(5, 2) == 10


def test_calculator_divide():
    """ tests multiplication of two numbers"""
    assert Calculator.divide_numbers(10, 2) == 5


def test_calculator_division_error():
    """ tests dividing by 0 exception """
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(10, 0) == 0


def test_empty_history(clear_history):
    """ tests the empty history function """
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.empty_history() is True
    assert Calculator.history_count() == 0


def test_count_history(clear_history):
    """ tests calculator storage """
    assert Calculator.history_count() == 0
    assert Calculator.add_number(4, 9) == 13
    assert Calculator.divide_numbers(50, 10) == 5
    assert Calculator.history_count() == 2


def test_last_calc_result():
    """ tests the calculators last stored value """
    assert Calculator.multiply_numbers(10, 2) == 20
    assert Calculator.subtract_number(15, 10) == 5
    assert Calculator.last_calc_to_history() == 5
    assert Calculator.empty_history() is True


def test_first_calc_result():
    """ tests the addition between 2 numbers """
    assert Calculator.add_number(100, 150) == 250
    assert Calculator.multiply_numbers(5, 5) == 25
    assert Calculator.first_calc_to_history() == 250
