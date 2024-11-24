import argparse
import os
from tkinter import filedialog
import csv
import validation
import pandas as pd

def search_medals(cntry, yr, cntry_raw):
    with open(os.getcwd() + "/" + args.filename, 'r') as file:
        next(file)
        data = []
        medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
        counter = 0
        for row in file:
            row = [int(i) if i.isdecimal() else i for i in row.split('\t')]
            if counter < 10:
                if row[7] == cntry and row[9] == int(yr):
                    if row[14][:-1] != 'NA':
                        data.append([row[1], row[12], row[14][:-1]])
                        medals[row[14][:-1]] += 1
                        counter += 1
            elif counter >= 10:
                if row[7] == cntry and row[9] == int(yr):
                    if row[14][:-1] != 'NA':
                        medals[row[14][:-1]] += 1

        data_formated = pd.DataFrame(data, columns=['Name', 'Sport', 'Medal'])
        print(data_formated)
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

def total_output(yr):
    with open(os.getcwd() + '/' + args.filename, 'r') as file:
        next(file)
        data = {}
        for row in file:
            row = [int(i) if i.isdecimal() else i for i in row.split('\t')]
            if row[9] == int(yr) and row[14][:-1] != 'NA':
                if row[7] not in data:
                    data[row[7]] = {"Gold" : 0, "Silver" : 0, "Bronze" : 0}
                    data[row[7]][row[14][:-1]] += 1
                else:
                    data[row[7]][row[14][:-1]] += 1
    pd.set_option('display.max_columns',None)
    pd.set_option('display.show_dimensions',False)
    print(pd.DataFrame(data))

def overall(cntries):
    all_years = {}
    for cntry in cntries:
        with open(args.filename, 'r') as file:
            next(file)
            all_years[cntry] = {}
            for row in file:
                row = [int(i) if i.isdecimal() else i for i in row.split('\t')]
                if row[7] == cntry and row[14][:-1] != 'NA':
                    if row[9] not in all_years[cntry]:
                        all_years[cntry][row[9]] = 1
                    else:
                        all_years[cntry][row[9]]+= 1

    best_years = []
    for cntry in all_years:
        best_year = 0
        for yr in all_years[cntry]:
            if best_year == 0 or all_years[cntry][yr] > all_years[cntry][best_year]:
                best_year = yr
        best_years.append([cntry, yr, all_years[cntry][best_year]])

    best_years_formated = pd.DataFrame(best_years, columns=['Country', 'Best year', 'Medals'])
    print(best_years_formated)

    if not args.output is None:
        path = filedialog.askdirectory()
        with open(path + '/' + args.output[0], 'w', newline='') as output:
            writer = csv.writer(output)
            header = ['Country', 'Best year', 'Medals']
            writer.writerow(header)
            for row in best_years:
                writer.writerow(row)


parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help='The path to the file with data')
parser.add_argument('-medals', '--medals', type=str, nargs=2, help="Enter '-medals country year' to see the particular country's result")
parser.add_argument('-output', '--output', type=str, nargs=1, help="Enter '-output filename.csv' to import output in a file")
parser.add_argument('-total', '--total', type=int, nargs=1, help="Enter '-total year' to see the total result of Olympics")
parser.add_argument('-overall', '--overall', type=str, nargs='*', help="Enter '-overall country country...' to see the most successful year for each country")
parser.add_argument('--interactive', action='store_true', help="Enter '--interactive' to switch to the interactive mode (where you can enter the country and see its stats)")
args = parser.parse_args()

if not args.medals is None:
    country = args.medals[0][:3].upper()
    if not validation.validation_country(country):
        quit()
    country = validation.validation_country(country)
    year = args.medals[1]
    if not validation.year_validation(year):
        quit()
    search_medals(country, year, args.medals[0])

if not args.total is None:
    year = args.total[0]
    if not validation.year_validation(year):
        quit()
    total_output(year)

if not args.overall is None:
    countries = [i for i in args.overall]
    countries_processed = []
    for country in countries:
        if not validation.validation_country(country):
            quit()
        else:
            countries_processed.append(validation.validation_country(country))

    overall(countries_processed)


#Tasks, needed to complete the level 1: think about formating the output into a table)
#Make overall output in table