"""
    Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário 
        é um palíndromo (lê-se igual de trás para frente).
"""

def obter_palavra() -> str:
    while True:
        try:
            return input("Informe 1 palavra: ")
        except:
            print("Palavra Inválida")

def eh_palindromo(palavra: str) -> bool:
    return palavra[::-1].upper() == palavra.upper()

palavra = obter_palavra()
palindromo = eh_palindromo(palavra)
texto_palindromo = " é " if palindromo else " não é "
print(f"A palavra \"{palavra}\" {texto_palindromo} 1 palíndromo")

