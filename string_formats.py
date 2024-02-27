from math import ceil

def format_to_max_one_decimal_place(number):
    if isinstance(number, float) or isinstance(number, int):
        one_decimal_place_str = "{:.1f}".format(number)
        one_decimal_place_float = float(one_decimal_place_str)
        if float(one_decimal_place_float) == ceil(one_decimal_place_float):
            return int(one_decimal_place_float)
        else:
            return one_decimal_place_str
    else:
        return number
