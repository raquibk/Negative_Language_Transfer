# Modules
import spacy
import pandas as pd

# Method of comparing: I am using spacy to read each sentence, do the tagging. I am then appending the tags
#                      of the sentence to a list. This procedure is done for Chinese, and English separately

# Loading taggers
nlp = spacy.load("en_core_web_sm")
nlp1 = spacy.load("zh_core_web_sm")

# Loading csv
df = pd.read_csv('globalvoices_sentences.csv')
df1 = pd.read_csv('tagged_globalvoices_sentences.csv')

# Variables used to store tag sequence of a sentence
en_ud = ""
en_penn = ""
ch_ud = ""
ch_penn = ""

# Used to count the discrepancies
en_count = 0 
ch_count = 0 

# Lists to which the tag sequences of each sentence are appended
en_ud_list = []
ch_ud_list = []
en_penn_list = []
ch_penn_list = []

for i in range(100):
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
    
    # Append English tag sequences
    en_ud_list.append(en_ud)
    en_penn_list.append(en_penn)

    for token in doc1:
        ch_penn += token.tag_
        ch_penn += " "
        ch_ud += token.pos_
        ch_ud += " " 
    # Append English tag sequences
    ch_ud_list.append(ch_ud)
    ch_penn_list.append(ch_penn)


# Count unequal strings
for i in range(100):
    if en_ud_list[i] != df1['en_ud'][i]:
        en_count += 1
    if ch_ud_list[i] != df1['zhs_ud'][i]:
        ch_count += 1

    

print("The number of english discrepancies: " + str(en_count))
print("The number of chinese discrepancies: " + str(ch_count))