import re


def contar_vogais(texto):
    # Define o padrão para encontrar vogais
    padrao = r'[aeiouAEIOU]'  # Procura por qualquer uma das vogais (maiúsculas ou minúsculas)

    # Encontra todas as vogais no texto
    vogais_encontradas = re.findall(padrao, texto)

    # Retorna o número de vogais encontradas
    return len(vogais_encontradas)


# Exemplo de uso:
texto = "Esta é uma frase com várias vogais."
total_vogais = contar_vogais(texto)
print("Total de vogais:", total_vogais)