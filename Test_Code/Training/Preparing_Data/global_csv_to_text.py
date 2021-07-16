import pandas as pd
import numpy as np

df = pd.read_csv('../../Resources/repaired_output.csv')

en_ud = df['en_ud']
zhs_ud = df['zhs_ud']

np.savetxt(r'../../Resources/zhs_ud.txt', zhs_ud.values, fmt='%s')
np.savetxt(r'../../Resources/en_ud.txt', en_ud.values, fmt='%s')