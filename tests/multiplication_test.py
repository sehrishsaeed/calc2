"""Testing Multiplication"""
from calc.Calculations.multiply import Multiplication


def test_calculation_subtraction():
    """testing that our calculator has a static method for multiplication"""
    # Arrange
    mynumbers = (1.0, 2.0)
    multiplication = Multiplication(mynumbers)
    # Act
    # Assert
    assert multiplication.get_result() == 2.0