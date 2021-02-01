# _*_ coding:utf-8 _*_
import pandas as pd
import tabula
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
            tabula.convert_into(pdffile, self.name, pages='all')

    def convert(self, column):
        ntype = []
        for translate in column:
            cvstr = str(translate)
            transl = cvstr.replace(',', '.').replace('nan', '0')
            ntype.append(float(transl))
        b = 0
        for cnvscores in ntype:
            b = b+cnvscores
            roundCScore = round(b/len(ntype))
            normalCScore = b/len(ntype)
        os.system('cls')
        print('Round:   ', roundCScore, '\nAverage: ', normalCScore)

    def averageScore(self):
        df = pd.read_csv(self.name)
        z = dict(enumerate(df.columns.values, start=1))  # 1
        print(z)
        nmbr = int(input('Enter number: '))
        columName = z[nmbr]
        df1 = df[columName].values.tolist()  # 2
        r = re.compile(',')
        if df[columName].dtype == 'object' or 'int':  # 3
            if any(r.search(str(comma)) for comma in df1) is True:  # 4
                df.fillna(0, inplace=True)
                self.convert(df1)
            else:
                df[columName] = pd.to_numeric(df[columName], errors='coerce')  # 5
                df.fillna(0, inplace=True)  # 6
                df1 = df[columName].values.tolist()
                a = 0
                for scores in df1:
                    a = a+scores
                roundScore = round(a/len(df1))
                normalScore = a/len(df1)
                os.system('cls')
                print('Round:   ', roundScore, '\nAverage: ', normalScore)


pdfTableValues().averageScore()


# 1 = Get column names
# 2 = Convert column values to list
# 3 = Check types of column values
# 4 = Search for comma in list to find float value that is string
# 5 = errors='coerce' instead of 'ignore' : https://towardsdatascience.com/how-to-change-datatypes-in-pandas-in-4-minutes-677addf9a409
# 6 = Fill all NaN values by 0
