import os
import pandas as pd


DIR = r'D:\script\Python-Learning\FileHandling\Excel'
excelFile = os.path.join(DIR, 'WikiCitation.xlsx')

data = pd.read_excel(excelFile)
df = pd.DataFrame(data, columns=['RefNum', 'Title', 'URL', 'Date'])


print(df.RefNum)
print(df.Title)
