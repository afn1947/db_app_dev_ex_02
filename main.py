import re
import time

"""
Exercise #2 
Database application development
9/4/2020
author: Avery Nutting-Hartman
"""


def transform_data():
    """
    Pulls the first name, last name, and gender from mockData.csv file and
    outputs it in json to 'YYYYMMDD'.csv file
    """
    file = open('mockData.csv', 'r', encoding='utf-8')
    output_file = open(time.strftime('%Y%m%d') + '.json', 'w+', encoding='utf-8')
    lines = file.readlines()
    lines = lines[1:]  # eliminate header row
    output_file.write("[\n")
    email_pattern = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+')  # regex to match an email
    for line in lines:
        line_list = line.strip().split(',')
        fname = line_list[1]
        lname = line_list[2]
        gender = line_list[4] if email_pattern.match(line_list[3]) else line_list[5]
        gender = 'Female' if 'f' in gender.lower() else 'Male'
        x = ('{"fname":"' + fname + '","lname":"' + lname + '","gender":"' + gender + '"},\n')
        if lines.index(line) == len(lines) - 1:  # -1 for the header line
            x = x[:-2]  # remove comma and new line from last entry
        output_file.write(x)
    output_file.write("\n]")
    output_file.close()
    file.close()


if __name__ == '__main__':
    transform_data()
