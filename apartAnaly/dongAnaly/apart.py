import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

apt_df = pd.read_csv('../resources/아파트_실거래가_2011-2020.csv',
                     encoding='cp949')

apt_df.rename(columns={'연도':'year',
                       '행정구역(동)':'area',
                       '1㎡당 가격':'price'},
                inplace=True)

print(type(apt_df['price'][118]))

condition = apt_df['area'] == '개포동'

xValues = apt_df['year'].unique()
yValues = apt_df[condition]['price']
areaList = apt_df['area'].unique()
for areaValue in areaList:
    condition = apt_df['area'] == areaValue
    yValues = apt_df[condition]['price']


    plt.plot(xValues, yValues, label = areaValue)
    plt.legend()
    plt.rc('font', family='Malgun Gothic')
plt.show()
