# Modules
import spacy
import pandas as pd
import numpy as np

# Method of comparing: I am using spacy to read each sentence, do the tagging. I am then appending the tags
#                      of the sentence to a list. This procedure is done for Chinese, and English separately

# Loading taggers

nlp = spacy.load("en_core_web_sm")
nlp1 = spacy.load("zh_core_web_sm")

# Loading csv
df = pd.read_csv('../../Resources/wmt-news_en-zh.csv')
output = pd.DataFrame(columns=['english', 'chinese', 'en_ud', 'en_penn', 'ch_ud', 'ch_penn'])

# Cleaning dataset
df['zhs'].replace('', np.nan, inplace=True)
df['en'].replace('', np.nan, inplace=True)
df.dropna(how = 'any', inplace= True)


# Variables used to store tag sequence of a sentence
total_rows = len(df.index)
en_ud = ""
en_penn = ""
ch_ud = ""
ch_penn = ""

for i in range(total_rows):
    try:
        print(i)
        en_ud = ""
        en_penn = ""
        ch_ud = ""
        ch_penn = ""
        # Make nlp object of sentence in Chinese and English
        doc = nlp(df['en'][i])
        doc1 = nlp1(df['zhs'][i])
        for token in doc:
            en_penn += token.tag_
            en_penn += " "
            en_ud += token.pos_
            en_ud += " " 

        for token in doc1:
            ch_penn += token.tag_
            ch_penn += " "
            ch_ud += token.pos_
            ch_ud += " " 

        output.loc[i] = [df['en'][i], df['zhs'][i], en_ud, en_penn, ch_ud, ch_penn]
    
    except KeyError as error:
        continue

en_ud = output['en_ud']
zhs_ud = output['ch_ud']

np.savetxt(r'../../Resources/wmt_zhs_ud.txt', zhs_ud.values, fmt='%s')
np.savetxt(r'../../Resources/wmt_en_ud.txt', en_ud.values, fmt='%s')