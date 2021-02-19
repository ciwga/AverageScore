# _*_ coding:utf-8 _*_
import pandas as pd
from tabula.io import convert_into
import os
import re


class pdfTableValues():

    def __init__(self):
        pdffile = input('Pdf Location: ')
        self.name = os.path.basename(pdffile)
        self.name = self.name.replace('pdf', 'csv')
        # findSpan = re.search('[a-zA-Z0-9]*.pdf$', pdffile)
        # spanLocation = [i for i in findSpan.span()]
        # spoint = spanLocation[0]
        # epoint = spanLocation[1]-4
        # self.outputName = pdffile[spoint:epoint]+'.csv'
        if os.path.isfile(self.name):
            pass
        else:
            convert_into(pdffile, self.name, pages='all')

    def calculater(self, data, name):
        a = 0
        query = "What is the percentage effect of the exam? (Like 0.30): "
        per = float(input(query))  # 7
        for cvScores in data:
            a = a+(cvScores*float(per))
            roundScore = round(a/len(data))
            normalScore = a/len(data)
        os.system('cls')
        print(f"{name} Round Average: {roundScore}\
              \n{name} Average: {normalScore}")

    def convert(self, column):
        ntype = []
        for translate in column:
            cvstr = str(translate)
            transl = cvstr.replace(',', '.').replace('nan', '0')
            ntype.append(float(transl))
        self.calculater(ntype)

    def averageScore(self):
        df = pd.read_csv(self.name)
        for names in range(1, len(df.columns.values)+1):
            z = dict(enumerate(df.columns.values, start=1))  # 1
        # print(z)
        # nmbr = int(input('Enter number: '))
            columName = z[names]
            df1 = df[columName].values.tolist()  # 2
            r = re.compile(',')
            if df[columName].dtype == 'object' or 'int':  # 3
                if any(r.search(str(comma)) for comma in df1) is True:  # 4
                    df.fillna(0, inplace=True)
                    self.convert(df1)
                else:
                    c = 'coerce'
                    df[columName] = pd.to_numeric(df[columName], errors=c)  # 5
                    df.fillna(0, inplace=True)  # 6
                    df1 = df[columName].values.tolist()
                    self.calculater(df1, columName)


pdfTableValues().averageScore()


# 1 = Get column names
# 2 = Convert column values to list
# 3 = Check types of column values
# 4 = Search for comma in list to find float value that is string
# 5 = errors='coerce' instead of 'ignore' : https://towardsdatascience.com/how-to-change-datatypes-in-pandas-in-4-minutes-677addf9a409
# 6 = Fill all NaN values by 0
# 7 = Only write 1 if you want to calculate only a lesson average score
