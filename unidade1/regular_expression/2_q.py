import re

def validar_email_UFC(email):
    padrao = r'^[\w\.-]+@ufc\.br$'  # Expressão regular para validar um endereço de email da UFC
    if re.match(padrao, email):
        return True
    else:
        return False

# Solicitar ao usuário que insira
email_usuario = input("Por favor, insira o seu email: ")

# Verificar o
if validar_email_UFC(email_usuario):
    print("O email pertence à Universidade Federal do Ceará (UFC).")
else:
    print("O email não pertence à Universidade Federal do Ceará (UFC).")
