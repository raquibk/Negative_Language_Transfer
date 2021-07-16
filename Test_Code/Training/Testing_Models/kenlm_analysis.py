from typing import Type
import kenlm
import string
import pandas as pd

model_en = kenlm.Model('../../Resources/n_gram_models/5_en.arpa')
model_zhs = kenlm.Model('../../Resources/n_gram_models/5_zhs.arpa')
df = pd.read_csv('../../../Testing_Set/processed_data.csv')


print(df['Incorrect UD Bigram'][2545])
false_positive = 0
false_negative = 0
true_positive = 0
true_negative = 0
type_errors = 0
for i in range(len(df.index)):
    try:
        tag = ""
        tag = df['Incorrect UD Bigram'][i]
        if model_en.score(tag) <  model_zhs.score(tag):
            if df['Negative Transfer'][i] == 'N':
                false_positive += 1
            elif df['Negative Transfer'][i] == 'Y':
                true_positive += 1

        elif model_en.score(tag) >  model_zhs.score(tag):
            if df['Negative Transfer'][i] == 'N':
                true_negative += 1
            elif df['Negative Transfer'][i] == 'Y':
                false_negative += 1            

    except TypeError:
        type_errors += 1

print('---------------------')
print('| Confusion Matrix                             |')
print('| True Positive: ' + str(true_positive)+ '| False Negative: ' + str(false_negative) + ' |')
print('| False Positive: ' + str(false_positive) + '| True Negative: ' + str(false_negative) + ' |')
print('---------------------')
print('Precision:')
print(true_positive/(true_positive+false_positive))
print('Recall:')
print(true_positive/(true_positive+false_negative))
print('F1: ')
print((2*))