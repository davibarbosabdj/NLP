from enelvo.normaliser import Normaliser

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")
nltk.download("omw-1.4")

import polars as pl
import pandas as pd


norm = Normaliser(
    tokenizer = 'readable',
    capitalize_inis = True,
    capitalize_pns = True,
    capitalize_acs = True,
    sanitize = True 
    )

# Texto

texto = """
n me mostre isso, por favor,
n sei, pergunta a sua mãe
Acho q tá bom, na hora lá tu n vai ler tudo, só explicar, mas deixa assim para caso eles forem estudar sozinhos depois,
pra que isso
        """
txt_normal = norm.normalise(texto)

## Token
nltk.download('stopwords')
stopwords = stopwords.words('portuguese')
texto_tokens = word_tokenize(texto)

texto_tk = [word for word in texto_tokens if not word in stopwords]

## Stemming

texto_stem = list()
sno = nltk.stem.SnowballStemmer('portuguese')
for word in texto_tk:
    word_stem = sno.stem(word)
    texto_stem.append(word_stem)
    

## Lematização
texto_lema = list()
wnl = WordNetLemmatizer()
for word in texto_stem:
    pl = wnl.lemmatize(word, pos="v")
    texto_lema.append(pl)

# Dataframe

dt = {
    "token" : [texto_tk],
    "Stemming" : [texto_stem],
    "Lemma" : [texto_lema]
}

dt_pl = pd.DataFrame(dt)

print(dt_pl)
