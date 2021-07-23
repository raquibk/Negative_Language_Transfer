from numpy import floor
import pandas as pd
from pandas.core.indexes.base import Index

en_df = pd.read_csv('../Resources/en_ud.txt')
zhs_df = pd.read_csv('../Resources/zhs_ud.txt')
new_en_df = '_en'
new_zhs_df = '_zhs'
upperbound = -999
lowerbound = 0
df_length = len(en_df.index)

for i in range(1,6):
    upperbound = int(floor((df_length/5)*i))
    print(len(en_df.iloc[lowerbound:upperbound].index))
    zhs_df.iloc[lowerbound:upperbound]
    lowerbound = upperbound

