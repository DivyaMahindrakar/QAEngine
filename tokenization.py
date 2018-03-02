import spacy
import en_core_web_sm
nlp=en_core_web_sm.load()
a=['I am','Who are','tell me','mumbai uni.']
z=[]

for item in a:
    row=[]
    for token in nlp(item):
        row.append(token.orth_)
    z.append(row)
  
print(z)
