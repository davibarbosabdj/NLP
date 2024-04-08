import re


def validar_senha(senha):
    """
    Função para validar se uma senha é segura ou não.

    Condições para uma senha segura:
    - Pelo menos 8 caracteres de comprimento.
    - Pelo menos uma letra minúscula.
    - Pelo menos uma letra maiúscula.
    - Pelo menos um dígito numérico.
    - Pelo menos um dos seguintes caracteres especiais: @, $, !, %, *, ?, &.
    """
    # Define o padrão para validar uma senha segura
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    # Verifica se a senha corresponde ao padrão
    if re.match(padrao, senha):
        return True
    else:
        return False


# Exibir as condições para uma senha segura
print("Para uma senha ser segura, ela deve atender aos seguintes critérios:")
print("- Pelo menos 8 caracteres de comprimento.")
print("- Pelo menos uma letra minúscula.")
print("- Pelo menos uma letra maiúscula.")
print("- Pelo menos um dígito numérico.")
print("- Pelo menos um dos seguintes caracteres especiais: @, $, !, %, *, ?, &.")

# Solicitar ao usuário que insira a senha
senha_usuario = input("Por favor, insira a senha a ser validada: ")

# Verificar se a senha inserida é segura
if validar_senha(senha_usuario):
    print("A senha inserida é segura.")
else:
    print("A senha inserida não é segura. Por favor, certifique-se de que ela atenda aos critérios mencionados acima.")
