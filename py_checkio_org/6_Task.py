# You have a string that consist only of digits.
# You need to find how many zero digits ("0") are at the beginning of the given string.
# Input: A string, that consist of digits.
# Output: An Int.
# Example:
# beginning_zeros('100') == 0
# beginning_zeros('001') == 2
# beginning_zeros('100100') == 0
# beginning_zeros('001001') == 2
# beginning_zeros('012345679') == 1
# beginning_zeros('0000') == 4


def beginning_zeros(number: str) -> int:
    result = []
    if number[0] != '0':
        return 0
    for number in number:
        if number == '0':
            result.append(number)
        elif number != '0':
            break
    return result.count('0')


print(beginning_zeros('10000'))


# Second solution
def beginning_zeros_second(number: str) -> int:
    count = len(number) - len(number.lstrip('0'))
    return count


print(beginning_zeros_second('0000'))
