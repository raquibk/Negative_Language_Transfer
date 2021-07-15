from typing import Type
import kenlm
import pandas as pd

model_en = kenlm.Model('../../Resources/n_gram_models/5_en.arpa')
model_zhs = kenlm.Model('../../Resources/n_gram_models/5_zhs.arpa')
df = pd.read_csv('../../../Testing_Set/processed_data.csv')


print(df['Incorrect UD Bigram'][2545])
count = 0
type_errors = 0
for i in range(len(df.index)):
    print(i)
    try:
        str = ""
        str = df['Incorrect UD Bigram'][i]
        if model_en.score(str, bos = True, eos = True) <  model_zhs.score(str, bos = True, eos = True):
            if df['Negative Transfer'][i] == 'N':
                count += 1
    except TypeError:
        type_errors += 1

print(count)
print(type_errors)