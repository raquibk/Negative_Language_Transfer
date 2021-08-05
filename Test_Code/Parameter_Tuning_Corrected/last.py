import pandas as pd
import numpy as np
from numpy import floor
en_df = pd.read_csv('en_ud.txt')
zhs_df = pd.read_csv('zhs_ud.txt')
upperbound = -999
lowerbound = 0
df_length = len(en_df.index)

for i in range(1,6):
    upperbound = int(floor((df_length/5)*i))
    en_pf = en_df.iloc[lowerbound:upperbound]
    zhs_pf = zhs_df.iloc[lowerbound:upperbound]
    np.savetxt(r'English/{}_en.txt'.format(i), en_pf.values, fmt="%s")
    np.savetxt(r'Chinese/{}_zhs.txt'.format(i), zhs_pf.values, fmt="%s")
    lowerbound = upperbound
