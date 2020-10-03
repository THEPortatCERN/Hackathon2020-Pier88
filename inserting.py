#!/usr/bin/python

import sqlite3
import pandas as pd
import numpy as np
from unchained import *



data = pd.read_excel(
    '2020ListofGoodsExcel.xlsx',
    sheet_name='Sheet1',
    header=0)



data['CL']=data['CL'].replace('X', 1)
data['CL']=data['CL'].replace(np.nan, 0)

data['FL']=data['FL'].replace('X', 1)
data['FL']=data['FL'].replace(np.nan, 0)


print(data)
conn = sqlite3.connect("unchained.db")

data.to_sql('unchained', conn, if_exists='replace', index=True, index_label='ID')
print("check")
show()

conn.close()

