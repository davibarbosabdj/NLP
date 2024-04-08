import re


def extrair_palavras(texto):
    # Define o padrão para encontrar palavras
    padrao = r'\b\w+\b'  # \b é usado para encontrar o limite de uma palavra

    # Encontra todas as palavras no texto
    palavras_encontradas = re.findall(padrao, texto)
    return palavras_encontradas


# Exemplo de uso:
texto = "Esta é uma string de exemplo, com várias palavras diferentes."
palavras = extrair_palavras(texto)
print(palavras)