""" This is the increment function"""
from calc.Calculations.addition import Addition
from calc.Calculations.division import Division
from calc.Calculations.subtract import Subtraction
from calc.Calculations.multiply import Multiplication
from calc.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def divide_numbers(*args):
        """ division number from result"""
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()