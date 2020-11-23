string = 'abttba'

if len(string) % 2 == 0:
    two_parts = len(string) / 2
    print(f'This is a palindrome, first part {string[:int(two_parts)]}, second part {string[int(two_parts):]}')
else:
    print('A palindrome can only consist of an even number of elements by definition')