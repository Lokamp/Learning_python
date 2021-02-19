import csv
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

file_path_one = filedialog.askopenfilename()
file_path_two = filedialog.askopenfilename()


def read_file(first_file: str, second_file: str):
    with open(f'{first_file}', 'r') as first_file:
        first_list = []
        reader = csv.reader(first_file)
        for i in reader:
            first_list.append(''.join(i).split(';'))

    with open(f'{second_file}', 'r') as second_file:
        second_list = []
        reader = csv.reader(second_file)
        for i in reader:
            second_list.append(''.join(i).split(';'))

    with open('result.csv', mode='w') as f:
        print('В процессе...')
        for string_in_first_file in first_list:
            for string_in_second_file in second_list:
                if string_in_first_file[0] in string_in_second_file:
                    result_writer = csv.writer(f, delimiter=';')
                    result_writer.writerow(string_in_first_file)


read_file(file_path_one, file_path_two)
print('Готово')
