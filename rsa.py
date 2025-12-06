import random as rd # Importando a biblioteca random

def mdc(n1, n2): # Método de Euclides
    while(n2 != 0): # Enquanto n2 for diferente de 0 faça:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1

def gerar_chave_publica(n): # Método para gerar a chave pública
    while True:
        e = rd.randrange(2, n) # Gerando um número aleatório entre 2 e n
        if(mdc(n,e) == 1):
            return e

def gerar_chave_privada (totiente, e): # Método para gerar a chave privada
    d = 0
    while((d *e)% totiente != 1): # Enquanto d não for multiplo de e faça:
        d += 1
    return d

def cifrar (mensagem, e, n): # Método para cifrar a mensagem
    msg_cifrada = "" # Variável para armazenar a mensagem cifrada
    for letra in mensagem: # Para cada letra da mensagem faça:
        k = (ord(letra) ** e) % n # k recebe a letra cifrada
        msg_cifrada += chr(k) # Adiciona a letra cifrada na variável
    return msg_cifrada # Retorna a mensagem cifrada

def decifrar (mensagem, n, d): # Método para decifrar a mensagem
    msg_decifrada = "" # Variável para armazenar a mensagem decifrada
    for letra in mensagem: # Para cada letra da mensagem faça:
        k = (ord(letra) ** d % n) # k recebe a letra decifrada
        msg_decifrada += chr(k) # Adiciona a letra decifrada na variável
    return msg_decifrada # Retorna a mensagem decifrada

def rsa(): # Método principal
    msg = input("Digite a mensagem: ") # Recebe a mensagem
    p = 17
    q = 19
    n = p * q
    y = p-1
    x = q -1
    totiente = x * y
    e = gerar_chave_publica(totiente) # Gerando a chave pública
    print(f"Chave Pública: ({e},{n})") # Imprimindo a chave pública

    d = gerar_chave_privada(totiente, e) # Gerando a chave privada
    print(f"Chave Privada: ({d},{n})") # Imprimindo a chave privada 

    msg = cifrar(msg, e, n) # Cifrando a mensagem
    print("MENSAGEM CIFRADA: " + msg) # Imprimindo a mensagem cifrada 

    msg = decifrar(msg, n, d) # Decifrando a mensagem
    print("MENSAGEM DECIFRADA: " + msg) # Imprimindo a mensagem decifrada 

rsa() # Chamando o método principal 
print("Digno de nota máxima?") # Mensagem de despedida