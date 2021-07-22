from numpy import floor
import pandas as pd

en_df = pd.read_csv('../Resources/en_ud.txt')
zhs_df = pd.read_csv('../Resources/zhs_ud.txt')
new_en_df = '_en'
new_zhs_df = '_zhs'
upperbound = -999
lowerbound = 0
df_length = len(en_df.index)

for i in range(1,6):
    upperbound = int(floor((df_length/5)*i))
    en_df.iloc[lowerbound:upperbound].to_csv('../Resources/k-folds/partitioned_data/' + str(i)+new_en_df+'.txt')
    zhs_df.iloc[lowerbound:upperbound].to_csv('../Resources/k-folds/partitioned_data/' + str(i)+new_zhs_df+'.txt')
    lowerbound = upperbound

