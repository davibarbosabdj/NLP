import re


def extrair_urls(texto):
    # Define o padrão para encontrar URLs
    padrao = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

    # Encontra todas as URLs no texto
    urls_encontradas = re.findall(padrao, texto)
    return urls_encontradas


# Solicitar ao usuário que insira o texto
texto_usuario = input("Por favor, insira o texto contendo as URLs: ")

# Extrair URLs do texto inserido pelo usuário
urls_encontradas = extrair_urls(texto_usuario)

# Imprimir as URLs encontradas
print("URLs encontradas:")
for url in urls_encontradas:
    print(url)