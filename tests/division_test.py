"""Testing Division"""
from calc.Calculations.division import Division


def test_calculation_subtraction():
    """testing that our calculator has a static method for division"""
    # Arrange
    mynumbers = (1.0, 5.0)
    division = Division(mynumbers)
    # Act
    # Assert
    assert division.get_result() == 5.0