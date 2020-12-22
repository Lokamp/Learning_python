# Split the string into pairs of two characters.
# If the string contains an odd number of characters,
# then the missing second character of the final pair should be replaced with an underscore ('_').


# Первое решение
def split_pairs(string: str) -> list:
    if len(string) % 2 != 0:
        string += '_'
    result = []
    index = 0
    counter = 0
    for letter in string:
        if index != 0:
            counter += 1
        if counter % 2 == 0:
            index += 1
            concatenate_two_letter = letter + string[index]
            result.append(concatenate_two_letter)
            index += 1
    return result


print(split_pairs('yyy'))


# Второе решение - через функцию enumerate
def split_pairs_(string: str) -> list:
    if len(string) % 2 != 0:
        string += '_'
    result = []
    counter = 0

    for index, letter in enumerate(string):
        if index != 0:
            counter += 1
        if counter % 2 == 0:
            concatenate_two_letter = letter + string[index + 1]
            result.append(concatenate_two_letter)
    return result


print(split_pairs_('yyy'))
