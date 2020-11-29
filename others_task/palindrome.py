string = 'abttba'

if len(string) % 2 == 0:
    split_word_into_two_parts = len(string) / 2
    first_part = string[:int(split_word_into_two_parts)]
    second_part = string[int(split_word_into_two_parts):][::-1]
    if first_part == second_part:
        print(f'This is a palindrome, first part {first_part}, second part {second_part}')
    else:
        print('This is not palindrome')
else:
    print('A palindrome can only consist of an even number of elements by definition')
