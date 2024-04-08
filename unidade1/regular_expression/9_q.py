import re


def extrair_nomes_proprios(texto):
    # Define o padrão para encontrar nomes próprios
    padrao = r'\b[A-Z][a-z]*\b'  # Procura por palavras iniciadas com uma letra maiúscula seguida de letras minúsculas

    # Encontra todos os nomes próprios no texto
    nomes_proprios = re.findall(padrao, texto)
    return nomes_proprios


# Exemplo de uso:
texto = "Vitoria, Mateus, Arthur, Pedro e Caique foram ao jogo hoje."
nomes = extrair_nomes_proprios(texto)
print("Nomes próprios encontrados:")
print(nomes)