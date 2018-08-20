

'''Determine if an input number is Even or Odd'''


def activity01(num1):
    if num1 % 2 == 0:
        return "Even"
    return "Odd"


'''Return the sum of two input values'''


def activity02(iv_one, iv_two):
    return iv_one + iv_two


'''Given a list of integers, count how many are even'''


def activity03(num_list):
    count = 0
    for item in num_list:
        if item % 2 == 0 and type(item) is int:
            count += 1

    return count


'''Return the input string, backward'''


def activity04(input_string):
    return input_string[::-1]
