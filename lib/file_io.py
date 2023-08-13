import os

def write_file(file_name, file_content):
    filepath = f'{file_name}.txt'
    with open(filepath, mode='w', encoding='utf-8') as log_file:
        log_file.write(file_content)

def append_file(file_name, append_content):
    filepath = f'{file_name}.txt'
    with open(filepath, mode='a', encoding='utf-8') as log_file:
        log_file.write(append_content)

def read_file(file_name):
    filepath = f'{file_name}.txt'
    with open(filepath, encoding='utf-8') as log_file:
        return log_file.read()

