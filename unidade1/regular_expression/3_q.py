import re


def extrair_numeros_telefone(texto):
    # Define o padrão para números de telefone
    padrao = r'\b\d{2,3}\s?\d{4,5}-?\d{4}\b'  # Padrão para números de telefone com ou sem hífen

    # Encontra todos os números de telefone no texto
    numeros_telefone = re.findall(padrao, texto)
    return numeros_telefone


# Solicitar ao usuário que insira o texto
texto_usuario = input("Por favor, insira o texto contendo os números de telefone: ")

# Extrair números de telefone do texto inserido pelo usuário
numeros_encontrados = extrair_numeros_telefone(texto_usuario)

# Imprimir os números de telefone encontrados
print("Números de telefone encontrados:")
for numero in numeros_encontrados:
    print(numero)