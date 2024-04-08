import re

def contar_ocorrencias_python(texto):
    padrao = r'Python'  # Expressão regular para encontrar a palavra "Python"
    ocorrencias = re.findall(padrao, texto)
    return len(ocorrencias)

# Exemplo de uso:
texto = "Python é uma linguagem de programação poderosa. Python é amplamente usada em várias aplicações. e cada vez mais o Python esta sendo utilizado"
resultado = contar_ocorrencias_python(texto)
print("Número de ocorrências de 'Python':", resultado)