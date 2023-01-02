import string
alphabet = (string.ascii_lowercase)
alphabetinverse =(string.ascii_lowercase[::-1])
def ma_string():
    print("je suis un beau string")

ma_string()
print(alphabet)
print(alphabetinverse)

def addition():
    num1=40
    num2=2
    print(num1+num2)

addition()


def produit():
    num1=3
    num2=6
    print(num1*num2)

produit()

phrase=input("tu marques et je cherche: ")
chercheur=('e' in phrase)

if chercheur:
    print("Y'a un e mec... c'est pas bien t'es un mauvais garçon")
