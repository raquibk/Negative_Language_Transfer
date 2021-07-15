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
print("lengthhhhhhhhhhhh  " + str(len(df.index)))

error_type = []
Negative_Transfer = []
Reason = []
incorrect_ud_tags = []
incorrect_ud_tags_padded = []
incorrect_ud_tags_unigram = []
incorrect_ud_tags_bigram = []
incorrect_sentence = []
likely_reason = []
count = 0
print(len(df.index))

for i in range(len(df.index)):
    try:
        incorrect_ud_tags_unigram_list = []
        incorrect_ud_tags_bigram_list = []
        incorrect_ud_tags_padded_list = []
        incorrect_ud_tags_list = []
        incorrect_sentence.append(df['incorrect_sentence'][i])
        likely_reason.append(df['Likely reason for mistake'][i])
        Negative_Transfer.append(df['Negative transfer?'][i])
        error_type.append(df['error_type'][i])
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
            incorrect_ud_tags_bigram_list.append(tags[sep_index+2+int(df['error_length'][i])])
        except IndexError:
            pass
        incorrect_ud_tags_bigram.append(' '.join(incorrect_ud_tags_bigram_list))

    except KeyError:
        count+=1
        continue

print("Count is: " + str(count))
print("Length of dataframe is: " + str(len(df.index)))
output = pd.DataFrame(
    {
        'Incorrect Sentence': incorrect_sentence,
        'Error Type': error_type,
        'Negative Transfer': Negative_Transfer,
        'Likely Reason for Mistake': likely_reason,
        'Incorrect UD': incorrect_ud_tags,
        'Incorrect UD Padded': incorrect_ud_tags_padded,
        'Incorrect UD Unigram': incorrect_ud_tags_unigram,
        'Incorrect UD Bigram': incorrect_ud_tags_bigram
    }
)
print(len(output.index))
#output.to_csv('../../../Testing_Set/processed_data.csv')
