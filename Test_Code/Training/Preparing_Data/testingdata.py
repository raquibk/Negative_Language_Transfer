# Modules
from os import sep
import pandas as pd
import numpy as np
import spacy

nlp = spacy.load("en_core_web_sm")
df = pd.read_csv("../../../Testing_Set/main_chinese.csv")

df['error_length'].replace('', np.nan, inplace=True)
df.dropna(how = 'any', inplace= True)
df.dropna()

error_type = []
Negative_Transfer = []
Reason = []
incorrect_ud_tags = []
incorrect_ud_tags_padded = []
incorrect_ud_tags_unigram = []
incorrect_ud_tags_bigram = []
incorrect_sentence = []
count = 0

for i in range(3000):
    try:
        incorrect_ud_tags_unigram_list = []
        incorrect_ud_tags_bigram_list = []
        incorrect_ud_tags_padded_list = []
        incorrect_ud_tags_list = []
        doc = nlp(df['incorrect_sentence'][i])
        space_segmented = df['incorrect_sentence'][i].split(' ')
        sep_index = space_segmented.index('|')
        tags = [tag.pos_ for tag in doc]
        incorrect_ud_tags_list = tags[sep_index+1:(sep_index+1+int(df['error_length'][i]))]
        incorrect_ud_tags.append(' '.join(incorrect_ud_tags_list))

        incorrect_ud_tags_padded_list = incorrect_ud_tags_list.copy()
        incorrect_ud_tags_unigram_list = incorrect_ud_tags_list.copy()
        incorrect_ud_tags_bigram_list = incorrect_ud_tags_list.copy()
        
        try:
            incorrect_ud_tags_padded_list.insert(0, tags[sep_index-1])
        except IndexError:
            pass
        try:
            incorrect_ud_tags_padded_list.append(tags[sep_index+1+int(df['error_length'][i])])
        except IndexError:
            pass
        incorrect_ud_tags_padded.append(' '.join(incorrect_ud_tags_padded_list))

        try:
            incorrect_ud_tags_unigram_list.append(tags[sep_index+1+int(df['error_length'][i])])
        except IndexError:
            pass
        incorrect_ud_tags_unigram.append(' '.join(incorrect_ud_tags_unigram_list))

        try:
            incorrect_ud_tags_bigram_list.append(tags[sep_index+1+int(df['error_length'][i])])
        except IndexError:
            pass
        try:
            incorrect_ud_tags_bigram_list.append(tags[sep_index+2+int(df['error_length'][i])])
        except IndexError:
            pass
        incorrect_ud_tags_bigram.append(' '.join(incorrect_ud_tags_bigram_list))

    except KeyError:
        continue


print('--------------------')
print(incorrect_ud_tags[-1])
print('--------------------')
print(incorrect_ud_tags_padded[-1])
print('--------------------')
print(incorrect_ud_tags_unigram[-1])
print('--------------------')
print(incorrect_ud_tags_bigram[-1])
print('--------------------')
print(count)