import pandas as pd
import numpy as np

df = pd.read_csv('../../Resources/repaired_output.csv')

en_ud = df['en_ud']

np.savetxt(r'../../Resources/en_ud.txt', en_ud.values, fmt='%s')