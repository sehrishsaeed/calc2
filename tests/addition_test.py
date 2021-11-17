"""Testing Addition"""
from calc.Calculations.addition import Addition


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    # Arrange
    mynumbers = (4.0, 3.0)
    addition = Addition(mynumbers)
    # Act
    # Assert
    assert addition.get_result() == 7.0