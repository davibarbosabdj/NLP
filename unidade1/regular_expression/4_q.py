import re


def substituir_gato_por_cachorro(texto):
    # Define o padrão para encontrar a palavra "gato"
    padrao = r'\bgato\b'  # \b é usado para corresponder à palavra "gato" como uma palavra inteira

    # Substitui todas as ocorrências de "gato" por "cachorro" no texto
    texto_substituido = re.sub(padrao, 'cachorro', texto)
    return texto_substituido


# Exemplo de uso:
texto = "O gato está dormindo no telhado. O gato é um animal doméstico."
texto_substituido = substituir_gato_por_cachorro(texto)
print(texto_substituido)