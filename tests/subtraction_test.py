"""Testing Subtraction"""
from calc.Calculations.subtract import Subtraction


def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    # Arrange
    mynumbers = (1.0, 2.0)
    subtraction = Subtraction(mynumbers)
    # Act
    # Assert
    assert subtraction.get_result() == -3
