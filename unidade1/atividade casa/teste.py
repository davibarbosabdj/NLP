#test
!pip install enelvo
from enelvo.normaliser import Normaliser
import nltk
nltk.download('punkt')

from nltk.corpus import stopwords
nltk.download('stopwords')
import pandas as pd
from nltk.stem import PorterStemmer, WordNetLemmatizer


norm = Normaliser(tokenizer='readable')

# atividade

# 3)
# a) correção do texto
texto = 'Eu fui ao parke com minha familiya e brinqei muito!'
print('texto original: ', texto)

texto_corrigido = norm.normalise(texto)
print('texto corrigido: ', texto_corrigido)
# b) tokenização
tokens = nltk.word_tokenize(texto_corrigido)

# c) removendo stop words
stop_words = set(stopwords.words('portuguese'))
tokens_sem_stopwords = [token for token in tokens if token.lower() not in stop_words]


# d) tabela mostrando token, stemming e lematização
# stemming
stemmer = PorterStemmer()
tokens_stemming = [stemmer.stem(token) for token in tokens_sem_stopwords]

# lematização
lemmatizer = WordNetLemmatizer()
tokens_lem = [lemmatizer.lemmatize(token) for token in tokens_sem_stopwords]

df = pd.DataFrame({
    'tokens': [tokens],
    'stemming': [tokens_stemming],
    'lematização': [tokens_lem]
})

print(df.T)