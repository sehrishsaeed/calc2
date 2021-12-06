"""Testing the Calculator"""
import pytest
import pandas as pd
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from calc.Calculations.addition import Addition


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
    # You have to add the fixture function as a parameter to the test that you want to use it with


def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    csv_reader = pd.read_csv("tests/Addition.csv")
    for index, row in csv_reader.iterrows():
        values = (row.value1, row.value2)
        addition = Addition.create(values)
        addition_result = csv_reader["result"][index]
        assert addition.get_result() == addition_result


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    file = open("Subtraction.csv")
    csvreader = csv.reader(file)
    for row in csvreader:
        print(int(row[0]), int(row[1]))
        assert Calculator.subtract_numbers(int(row[0]), int(row[1])) == int(row[2])


def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    file = open("Multiply.csv")
    csvreader = csv.reader(file)
    for row in csvreader:
        print(int(row[0]), int(row[1]))
        assert Calculator.multiply_numbers(int(row[0]), int(row[1])) == int(row[2])


def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    file = open("Divide.csv")
    csvreader = csv.reader(file)
    for row in csvreader:
        print(int(row[0]), int(row[1]))
        assert Calculator.divide_numbers(int(row[0]), int(row[1])) == int(row[2])
