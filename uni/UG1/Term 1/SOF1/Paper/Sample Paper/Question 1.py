"""
1 (15 marks) Basic Programming Structure
The code must be written in the provided file question_1.py.
Implement a function to_barcode(binary) that takes a binary string (a string composed
of 0s and 1s only) as parameter and returns a string representing a bar-code. The 0s are
transformed into ’.’ and 1s into ’|’. For example:
to_barcode(’0010111’)
’..|.|||’
In addition, the function must return None if the string contains a character that is not a 0 or a 1.
We also assume that a string is always given, so you don’t need to check the type of the
parameter.
Finally, write the docstring for this function (5 marks). Note, the docstring must follow one of the
following guidelines; PEP 0257, NumPy, or Google documentation style.
"""

def to_barcode(binary_string):
    """Return binary string converted to barcode.

    Args:
        binary_string: string of 1s and 0s only
    Returns:
        bar_code: bariable contains string of |s and .s modelling a barcode,
        however if invalid character in binary_string comtains None.
"""
    bar_code = ""
    for char in binary_string:
        if char == '0':
            bar_code += '.'
        elif char == '1':
            bar_code += '|'
        elif char == '' or ' ':
            return None
        else:
            raise ValueError
    return bar_code