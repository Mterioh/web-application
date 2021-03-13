#  Copyright (c) 2021.
#  Vyacheslav Shchurov
#  diskoknife@gmail.com

"""

*Put some description for this file here*

"""
import re
import smtplib

def main():
    filename = input("Enter the name of message you will send:\n")
    read_message_file(filename)

def read_message_file(file):
    return file


# Patterns for regex
find_email = re.compile(r"(\w+[\._]|\w+)(@)(\w+(\.)\w+)")
find_name = re.compile(r"\w+ ")
def choose_recepients(file):
    names = []
    emails = []
    with open(file, 'r') as f:
        for line in f.readlines():
            names.append(find_name.search(line).group(0))
            emails.append(find_email.search(line).group(0))
    return names, emails


def auth_smtp_client(smtp, host=465):


if __name__ == '__main__':
    main()