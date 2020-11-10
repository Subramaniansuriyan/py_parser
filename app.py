from pathlib import Path
from bs4 import BeautifulSoup
import glob
import codecs
import sys
import os
import json
import components

def parse_file(dirpath):
    y=input("Enter name or case type :")

    files = []
    for file in Path(dirpath).rglob('*.html'):
        f=codecs.open(file, 'r')
        if y in f.read():
            files.append(file.name)
    if files == []:
        print("Try some other word")
    else:
        print("The first 5 files contains the string exactly:")
        print(files[:5])
        print("The list of file names :")
        print(files)


def parse_htmlfile(filepath):
    file_descriptor = open(filepath,"r")
    print("Output: ", parse_html(file_descriptor))


def parse_html(f):
    soup = BeautifulSoup(f.read(), "html.parser")
    context = {}
    
    context['case_details'] = components.parse_case_details(soup)
    context['case_status'] = components.parse_case_status(soup)
    context['petitoner_and_advocate'] = components.parse_petitoner_and_advocate(soup)
    context['respondent_and_advocate'] = components.parse_respondent_and_advocate(soup)
    context['acts'] = components.parse_acts_table(soup)
    context['history'] = components.parse_history_table(soup)
    context['orders'] = components.parse_orders_table(soup)

    return context


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
        if os.path.isdir(arg):
            parse_file(arg)
        else:
            parse_htmlfile(arg)
    except Exception as e:
        print ("usage: python app.py directory_path|file_path")





