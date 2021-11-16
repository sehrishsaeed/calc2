"""Calculation history Class"""
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class Calculations:
    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        return Calculations.history[-1]

    @staticmethod
    def get_calculation(num):
        """ gets calc from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """" gets calc from history"""
        return Calculations.history.append(calculation)
