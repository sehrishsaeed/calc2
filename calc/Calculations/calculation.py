"""This is our calculation base class/abstract class"""


class Calculation:
    """ calculation abstract base class"""
    # pylint: disable=too-few-public-methods
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b
        """ constructor method"""
        self.values = Calculation.convert_args_to_list_float(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float