'''Este é um algoritmo muito simples para a criptografia de uma mensagem de texto.
O algoritmo se baseia em somar uma chave numérica em cada uma dos caracteres da mensagem
 para embaralhar os caracteres.
O detalhe principal deste problema é a parte do módulo.'''
# INCOMPLETO!

def cesarCipherEncryption(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxz'
    encoded = ''

    for i in message:
        encoded_LetterIndex = ((ord(i) - ord('a')) + key)%26
        encoded += alphabet[encoded_LetterIndex]

    return encoded


def cesarCipherDecryption(crypto, key):
    pass


message = 'pedrofoicontratadohojemesmo'

cryptoMessage = cesarCipherEncryption(message, 10)

#decryptedMessage = cesarCipherDecryption(cryptoMessage, 10)

print(cryptoMessage)
#print(decryptedMessage)
