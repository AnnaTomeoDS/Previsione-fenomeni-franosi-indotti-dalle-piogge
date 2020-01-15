import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
df = pd.read_excel(r'C:\Users\annit\Desktop\TRMM_Ab.xlsx')
df.set_axis(['date', 'mean1', 'max1', 'mean2', 'max2', 'mean3', 'max3', 'mean4', 'max4', 'mean5', 'max5', 'mean6', 'max6'], axis='columns', inplace=True)
#print(df)
dfF = pd.read_excel(r'C:\Users\annit\Desktop\ab.xlsx')
dfF.set_axis(['date', 'zona1', 'zona2', 'zona3', 'zona4', 'zona5', 'zona6'], axis='columns', inplace=True)
df2 = pd.DataFrame(df)
#print(df2)
'''for i in df['date']:
 data_frana = i
 for j in dfF['date']:
  if(data_frana=='2010-06-15'):
      print(data_frana)
'''
#togliere le righe =0 nel daataset delle frane
dfprova = pd.read_excel(r'C:\Users\annit\Desktop\abprova.xlsx')
dfprova.set_axis(['date', 'zona1', 'zona2', 'zona3', 'zona4', 'zona5', 'zona6'], axis='columns', inplace=True)
print(dfprova)

value = '20/10/2010'
print(df.loc[df['date'] == value])
