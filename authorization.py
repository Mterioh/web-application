#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Write data in file (first name, last name and assignment identification number)

"""
import random
import os


def check_data_for_write(firstname: str, lastname: str):
    """
    This function checking checking for correctness of input data
    :param firstname: string consisting of letters of the English alphabet
    :param lastname: string consisting of letters of the English alphabet
    """
    for symbols in firstname:
        if chr(65) <= symbols <= chr(90) or chr(97) <= symbols <= chr(122):
            continue
        else:
            print("Error input data!")
            return False
    for symbols in lastname:
        if chr(65) <= symbols <= chr(90) or chr(97) <= symbols <= chr(122):
            continue
        else:
            print("Error input data!")
            return False
    return True


def test_file_for_emptiness():
    if check_data_for_write(enter_first_name, enter_first_name):
        check_file_empty = 'data.txt'
        result = os.stat(check_file_empty)
        if result.st_size != 0:
            additional_recording_data_file()
        else:
            write_data_in_empty_file()


def write_data_in_empty_file():
    """
    This function write data in file data.txt
    """
    file = open("data.txt", "w")
    file.write(enter_first_name + " ")
    file.write(enter_last_name + " ")
    file.write("#" + str(random.randint(1000000, 1000000000)))
    file.close()


def additional_recording_data_file():
    """
    If file data.txt not empty then add data
    :return:
    """
    file = open("data.txt", "a")
    file.write("\n" + enter_first_name + " ")
    file.write(enter_last_name + " ")
    file.write("#" + str(random.randint(1000000, 1000000000)))
    file.close()


while True:
    enter_first_name = str(input("Please, enter to your first name: "))
    enter_last_name = str(input("Please, enter to your last name:  "))
    if check_data_for_write(enter_first_name, enter_last_name):
        break

test_file_for_emptiness()
