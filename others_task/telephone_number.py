# Проверка ввода телефоного номера

telephone_number = input('Введите номер телефона без +7, используйте только цифры, пример: 9001000000 ')

while True:
    if telephone_number.isdigit() and len(telephone_number) == 10:
        print(f'Ваш номер телефона +7{telephone_number}')
    else:
        print('Вы неверно ввели номер телефона, необходимо ввести 10 цифр, пример: 9001000000 ')
