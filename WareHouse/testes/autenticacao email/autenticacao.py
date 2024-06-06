import win32com.client as win32
import random

def gerar_codigo():
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Escolhe o número de números e letras aleatoriamente
    num_numeros = random.randint(1, 5)
    num_letras = 5 - num_numeros

    # Escolhe os números e letras aleatoriamente
    numeros_aleatorios = random.sample(numeros, num_numeros)
    letras_aleatorias = random.sample(letras, num_letras)

    # Combina os números e letras em uma string
    string_aleatoria = ''.join(str(n) for n in numeros_aleatorios) + ''.join(letras_aleatorias)

    return string_aleatoria

def enviar_email(email_destino, cod):
    outlook = win32.Dispatch('outlook.application')
    email_obj = outlook.CreateItem(0)
    email_obj.To = email_destino
    email_obj.Subject = "Seu código de login"
    email_obj.HTMLBody = f"""
    <p>Olá, aqui é o código de validação</p>

    <p>O seu código de validação: {cod}</p>
    <p>Você tem 1 minuto</p>
    """
    email_obj.Send()
    print("Email Enviado")

def verificar_codigo(cod, cod_user):
    if cod_user == cod:
        return True
    else:
        return False

# Gerar o código
cod = gerar_codigo()

# Enviar o e-mail
emai = input('Digite seu email: ')
enviar_email(emai, cod)

# Verificar o código
cod_user = input('Digite o código que chegou em seu email: ')
if verificar_codigo(cod, cod_user):
    print('Código correto')
else:
    print('Código incorreto')