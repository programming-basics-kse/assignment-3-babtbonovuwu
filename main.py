import argparse
import os
from tkinter import filedialog
import csv

def search_medals(cntry, yr, cntry_raw):
    with open(args.filepath, 'r') as file:
        next(file)
        data = []
        medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
        print('Name----Sport----Medal')
        counter = 0
        for row in file:
            row = [int(i) if i.isdecimal() else i for i in row.split('\t')]
            if counter < 10:
                if row[7] == cntry and row[9] == int(yr):
                    if row[14][:-1] != 'NA':
                        data.append([row[1], row[12], row[14]])
                        print(f'{row[1]}----{row[12]}----{row[14]}', end='')
                        medals[row[14][:-1]] += 1
                        counter += 1
            elif counter >= 10:
                if row[7] == cntry and row[9] == int(yr):
                    if row[14][:-1] != 'NA':
                        medals[row[14][:-1]] += 1
        print()
        print(f"For year {yr}, {cntry_raw} has gained {medals['Gold']} gold medals, {medals['Silver']} silver medals and {medals['Bronze']} bronze medals")

        if not args.output is None:
            path = filedialog.askdirectory()
            with open(path + '/' + args.output[0], 'w', newline='') as output:
                writer = csv.writer(output)
                header = ['Name', 'Sport', 'Medal']
                writer.writerow(header)
                for i in data:
                    writer.writerow(i)
                writer.writerow([f"For year {yr}, {cntry_raw} has gained {medals['Gold']} gold medals, {medals['Silver']} silver medals and {medals['Bronze']} bronze medals"])


parser = argparse.ArgumentParser()
parser.add_argument('filepath', type=str, help='The path to the file with data')
parser.add_argument('-medals', '--medals', type=str, nargs=2, help="Enter '-medals country year' to see the particular country's result")
parser.add_argument('-output', '--output', type=str, nargs=1, help="Enter '-output filename.csv' to import output in a file")
parser.add_argument('-total', '--total', type=int, nargs=1, help="Enter '-total year' to see the total result of Olympics")
parser.add_argument('-overall', '--overall', type=str, nargs='*', help="Enter '-overall country country...' to see the most successful year for each country")
parser.add_argument('--interactive', action='store_true', help="Enter '--interactive' to switch to the interactive mode (where you can enter the country and see its stats)")
args = parser.parse_args()

if not args.medals is None:
    country = args.medals[0][:3].upper()
    year = args.medals[1]
    if not year.isdecimal():
        print("Year is invalid, please enter the decimal number (between 1904 and 2024)")
    search_medals(country, year, args.medals[0])

#Tasks, needed to complete the level 1: complete validation, add extreme cases (there was no olympics at entered year, entered country doesn't exist or doesn't have medalists, etc.), think about formating the output into a table, find out how to get the path normally (without printing the full path)
