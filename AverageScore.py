# _*_ coding:utf-8 _*_
import pandas as pd
import tabula
import os
import re

ntype = []


def convert(column):    # Convert string to float
    for translate in column:
        trans = translate.replace(',', '.')
        ntype.append(float(trans))
    b = 0
    for cnvscores in ntype:
        b = b+cnvscores
        roundCScore = round(b/len(ntype))
        normalCScore = b/len(ntype)
        os.system('cls')
        print('Round:   ', roundCScore, '\n', 'Average: ', normalCScore)


def average_score():    # Find average score for one lesson
    pdffile = input('Pdf Location: ')
    findSpan = re.search('[a-zA-Z0-9]*.pdf$', pdffile)
    tuple2list = [i for i in findSpan.span()]
    spoint = tuple2list[0]
    epoint = tuple2list[1]-4
    outputName = pdffile[spoint:epoint]+'.csv'
    if os.path.exists(outputName) == 'True':
        pass
    else:
        tabula.convert_into(pdffile, outputName, pages='all')

    df = pd.read_csv(outputName)
    z = dict(enumerate(df.columns.values, start=1))     # 1
    print(z)
    nmbr = int(input('Enter number: '))
    column_name = z[nmbr]
    df1 = df[column_name].values.tolist()   # 2
    r = re.compile(',')
    if df[column_name].dtype == 'object' or 'int':  # 3
        if any(r.search(str(comma)) for comma in df1) is True:  # 4
            df.fillna(0, inplace=True)
            convert(df1)
        else:
            df[column_name] = pd.to_numeric(df[column_name], errors='coerce')  # 5
            df.fillna(0, inplace=True)  # 6
            df1 = df[column_name].values.tolist()
            a = 0
            for scores in df1:
                a = a+scores
            roundScore = round(a/len(df1))
            normalScore = a/len(df1)
            os.system('cls')
            print('Round:   ', roundScore, '\n', 'Average: ', normalScore)


average_score()

# 1 = Get column names
# 2 = Convert column values to list
# 3 = Check types of column values
# 4 = Search for comma in list to find float value that is string
# 5 = errors='coerce' instead of 'ignore' : https://towardsdatascience.com/how-to-change-datatypes-in-pandas-in-4-minutes-677addf9a409
# 6 = Fill all NaN values by 0
