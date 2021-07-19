from typing import Type
import kenlm
import string
import pandas as pd

model_en = kenlm.Model('../../Resources/n_gram_models/5_en.arpa')
model_zhs = kenlm.Model('../../Resources/n_gram_models/5_zhs.arpa')
df = pd.read_csv('../../../Testing_Set/processed_data.csv')
error_set = pd.read_csv('../../Resources/error_type_meaning.csv')

false_positive = 0
false_negative = 0
true_positive = 0
true_negative = 0
type_errors = 0
errors = {}

for i in range(len(error_set.index)):
    if error_set['structural'][i] == True:
        errors[error_set['error_type'][i]] = True
    else:
        errors[error_set['error_type'][i]] = False        

for i in range(len(df.index)):
    if errors[df['Error Type'][i]] == True:
        try:
            tag = ""
            tag = df['Incorrect UD Padded'][i]
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

precision = true_positive/(true_positive+false_positive)
recall = true_positive/(true_positive+false_negative)
f1 = 2*((precision*recall)/(precision+recall))

print('---------------------')
print('| Confusion Matrix                             |')
print('| True Positive: ' + str(true_positive)+ '| False Negative: ' + str(false_negative) + ' |')
print('| False Positive: ' + str(false_positive) + '| True Negative: ' + str(true_negative) + ' |')
print('---------------------')
print('Precision:')
print(precision)
print('Recall:')
print(recall)
print('F1:')
print(f1)
print(true_negative+true_positive+false_negative+false_positive)