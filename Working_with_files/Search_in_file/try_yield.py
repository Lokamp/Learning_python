import csv
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

file_path_one = filedialog.askopenfilename()
file_path_two = filedialog.askopenfilename()


def read_file(file: str):
    with open(f'{file}', 'r') as file:
        reader = csv.reader(file)
        for string in reader:
            yield [str(word).lower() for word in ''.join(string).split(';')]


result = []
with open(f'{file_path_two}', 'r') as lis_file:
    lis_reader = list(csv.reader(lis_file))
    for i in lis_reader:
        result.append(i)


first_file = read_file(file_path_one)  # search in this file


with open('result.csv', mode='w') as f:
    for string_in_first_file in first_file:
        for string_in_second_file in result:
            if string_in_first_file[0] in string_in_second_file:
                result_writer = csv.writer(f, delimiter=';')
                result_writer.writerow(string_in_first_file)
