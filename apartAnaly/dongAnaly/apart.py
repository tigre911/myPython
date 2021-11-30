import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

apart_data = pd.read_csv('../resources/아파트_실거래가_2011-2020.csv',index_col=False, encoding='cp949', engine='python')


apart_data = pd.DataFrame(apart_data)

apart_data.rename(columns={'연도': 'year',
                          '행정구역(동)': 'area',
                          '1㎡당 가격':'price'},inplace=True)
print(type(apart_data.area.unique()))
dong_data = ['개포동', '논현동', '대치동', '도곡동', '삼성동', '세곡동', '수서동', '신사동', '압구정동', '역삼동', '일원동', '청담동']

for n in dong_data:
    print(n)

for i in range(12):
    condition = apart_data[apart_data.area == dong_data[i]]
    plt.plot(condition.year, condition.price, label = dong_data[i])

plt.show()

