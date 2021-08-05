import pandas as pd
import kenlm

filename = "6n_"
en_fileext = "en.arpa"
zhs_fileext = "zhs.arpa"
en_fullname = ""
zhs_fullname = ""
false_negative = 0
true_positive = 0
precisions = []

for i in range(1,6):
    false_negative = 0
    true_positive = 0
    en_fullname = filename + str(i) + en_fileext
    zhs_fullname = filename +str(i) + zhs_fileext
    model_en = kenlm.Model('LMs/'+en_fullname)
    model_zhs = kenlm.Model('LMs/'+zhs_fullname)
    en = open('English/{}_en.txt'.format(i)).readlines()
    zhs = open('Chinese/{}_zhs.txt'.format(i)).readlines()

    for tag in en:
        if model_en.score(tag) <  model_zhs.score(tag):
            false_negative+=1
        elif model_en.score(tag) >  model_zhs.score(tag):
            true_positive+=1

    for tag in zhs:
        if model_en.score(tag) >  model_zhs.score(tag):
            false_negative+=1
        elif model_en.score(tag) <  model_zhs.score(tag):
            true_positive+=1

    precisions.append(true_positive/(true_positive+false_negative))
    print('True Positives: {}'.format(true_positive))   
    print('False Negatives: {}'.format(false_negative))


print(precisions)