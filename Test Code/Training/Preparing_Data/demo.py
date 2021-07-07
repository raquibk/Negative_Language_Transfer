import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")
nlp1 = spacy.load("zh_core_web_sm")
df = pd.read_csv('globalvoices_sentences.csv')
df1 = pd.read_csv('tagged_globalvoices_sentences.csv')

