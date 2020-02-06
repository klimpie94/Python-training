# Create a divide_zero function that returns -1
# in case the user tries to divide a number by 0.
# This might throw a ZeroDivisonError.


def divide_zero_with_no_error(nominator, denominator):
    try:
        return nominator / denominator
    except ZeroDivisionError:
        return -1


print(divide_zero_with_no_error(90, 1))
