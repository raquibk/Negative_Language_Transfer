import kenlm
import spacy
model = kenlm.Model('../../Resources/n_gram_models/5_en.arpa')
model_zhs = kenlm.Model('../../Resources/n_gram_models/5_zhs.arpa')

nlp = spacy.load("en_core_web_sm")
doc = nlp("The idea of international art festival was great")
str = ""

for token in doc:
    str+= token.pos_
    str+= " "

print(str)
print(model.score(str, bos = True, eos = True))
print(model_zhs.score(str, bos = True, eos = True))