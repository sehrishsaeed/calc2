""" This is the increment function"""
from individual_calc.addition import Addition
from individual_calc.subtraction import Subtraction
from individual_calc.multiplication import Multiplication
from individual_calc.division import Division


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def first_calc_to_history():
        """ adds the first calculation to history """
        return Calculator.history[0].get_result()

    @staticmethod
    def empty_history():
        """ clears history function """
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """ however many calculations have been stored in the array """
        return len(Calculator.history)

    @staticmethod
    def add_to_history(calculation):
        """ adds the calculation to history when called """
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def last_calc_to_history():
        """ returns the last calc in the array """
        return Calculator.history[-1].get_result()

    @staticmethod
    def add_number(val_a, val_b):
        """ adds number to result"""
        Calculator.add_to_history(Addition.create(val_a, val_b))
        return Calculator.last_calc_to_history()

    @staticmethod
    def subtract_number(val_a, val_b):
        """ subtract number from result"""
        Calculator.add_to_history(Subtraction.create(val_a, val_b))
        return Calculator.last_calc_to_history()

    @staticmethod
    def multiply_numbers(val_a, val_b):
        """ multiply two numbers and store the result"""
        Calculator.add_to_history(Multiplication.create(val_a, val_b))
        return Calculator.last_calc_to_history()

    @staticmethod
    def divide_numbers(val_a, val_b):
        """divide two numbers and store the result"""
        Calculator.add_to_history(Division.create(val_a, val_b))
        return Calculator.last_calc_to_history()
