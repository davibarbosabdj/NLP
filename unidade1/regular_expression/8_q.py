import re


def validar_formato_data(data):
    # Define o padrão para validar o formato da data "DD/MM/AA"
    padrao = r'^\d{2}/\d{2}/\d{2}$'

    # Verifica se a data corresponde ao padrão
    if re.match(padrao, data):
        return True
    else:
        return False


# Solicitar ao usuário que insira a data
data_usuario = input("Por favor, insira a data no formato 'DD/MM/AA': ")

# Verificar se a data inserida está no formato correto
if validar_formato_data(data_usuario):
    print("A data inserida está no formato correto 'DD/MM/AA'.")
else:
    print("A data inserida não está no formato correto 'DD/MM/AA'.")