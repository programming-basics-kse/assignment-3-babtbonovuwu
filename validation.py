from os import getcwd
def validation_country(country):
    country = country.upper()
    full = []
    alp3 = []
    alp2 = []
    result = False
    with open(getcwd() + "/gubami.csv ", 'r') as nogami:
        next(nogami)
        for guby in nogami:
            guby = guby.split(',')
            full.append(guby[0].upper())
            alp3.append(guby[1].upper())
            alp2.append(guby[2].upper())
    if country not in full and country not in alp3 and country not in alp2:
        print('Such country is not included in the data set.')
    else:
        if len(country)==2:
            result = alp3[alp2.index(country)]
        elif len(country)==3:
            result = country
        else:
            result = alp3[full.index(country)]
    return result

def year_validation(year):
    with open(getcwd() + "/DataSet.tsv ", 'r') as nogami:
        next(nogami)
        years = set()
        for guby in nogami:
            guby = guby.split('\t')
            years.add(guby[9])
        if year not in years:
            print('Such year is not included in the data set.')
            return False
        else:
            return True
