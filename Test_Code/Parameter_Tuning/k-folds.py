import pandas as pd
import kenlm

filename = "4n_"
en_fileext = "en.arpa"
zhs_fileext = "zhs.arpa"
en_fullname = ""
zhs_fullname = ""

false_positive = 0
false_negative = 0
true_positive = 0
true_negative = 0
type_errors = 0

for i in range(1,6):
    en_fullname = filename + str(i) + en_fileext
    zhs_fullname = filename +str(i) + zhs_fileext
    model_en = kenlm.Model('../../Test_Code/Resources/k-folds/LMs/'+en_fullname)
    model_zhs = kenlm.Model('../../Test_Code/Resources/k-folds/LMs/'+zhs_fullname)
    en_df = pd.read_csv('../../Test_Code/Resources/k-folds/partitioned_data/raw_partition/' + str(i) + '_en.txt')
    zhs_df = pd.read_csv('../../Test_Code/Resources/k-folds/partitioned_data/raw_partition/' + str(i) + '_zhs.txt')

    for tag in en_df['ADP DET PROPN PROPN CCONJ NOUN PUNCT PROPN PROPN ']:
        if model_en.score(tag) <  model_zhs.score(tag):
            false_negative+=1
        elif model_en.score(tag) >  model_zhs.score(tag):
            true_positive+=1

    for tag in zhs_df['DET NOUN PUNCT ']:
        if model_en.score(tag) >  model_zhs.score(tag):
            false_negative+=1
        elif model_en.score(tag) <  model_zhs.score(tag):
            true_positive+=1

    


print(true_positive)
print(false_negative)