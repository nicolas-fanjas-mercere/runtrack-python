def ma_print_hello():
    print("hello word")

ma_print_hello()


def ma_print_name(name):
    print(name)

ma_print_name("xavier du ligonnés du pont")
ma_print_name("Nicolas")

def add(num1,num2):
    resultat=(num1 + num2)
    print(resultat)

add(4,5)

def getHello():
    hello="Hello la plateforme"
    return(hello)

print(getHello())


def calculed():
    oparator = (input("operator"))
    if oparator == ("-"):
        num1=int(input("1ernumero à sosutraire"))
        num2=int(input("2eme numero à sosutraire"))
        resultatsous=(num1 - num2)
        return(resultatsous)

    elif oparator == ("+"):
        num1=int(input("1ernumero à additioner"))
        num2=int(input("2eme numero à additioner"))
        resultatadd=(num1 + num2)
        return(resultatadd)

    elif oparator == (""):
        num1=int(input("1ernumero à multiplier"))
        num2=int(input("2eme numero à multiplier"))
        resultatamulti=(num1 num2)
        return(resultatamulti)

    elif oparator == ("/"):
        num1 = int(input("1ernumero à diviser"))
        num2 = int(input("2eme numero à diviser"))
        resultatdivision=(num1 / num2)
        return(resultatdivision)



print(calculed())


def calcule(num1, operator, num2):
    if operator == "+":
     return num1 + num2
    elif operator == "-":
     return num1 - num2
    elif operator == "":
     return num1 num2
    elif operator == "/":
     return num1 / num2
    elif operator == "%":
     return num1 % num2

print(calcule(10,"+", 3))
print(calcule(10,"-", 3))
print(calcule(10,"*", 3))
print(calcule(10,"/", 3))
print(calcule(10,"%", 3))






def nombre(chiffre):
  if (chiffre<0):
    print('ton chiffre il est negatif')
  elif (chiffre >0):
    print(" ton chiffre il est positif")

nombre(-8)




def langage(langage):
    if (langage == ("javascript")):
        print ("tu es un developpeur web")

    elif (langage == ("python")):
        print("ia")

    elif (langage == ("java")):
        print("tu es un developpeur logiciel")

    elif (langage == ("reactjs")):
        print("tu es un developpeur mobile")

langage("python")


def saison(type,saison):
    if (type == ("fruits") and saison == ("hiver")):
        print ("orange, mandarine et kiwi")

    elif (type == ("fruits") and saison == ("ete")):
        print ("pore, fraise et cassis")

    elif (type == ("legumes") and saison == ("hiver")):
        print ("carrote, topinombour, endive et kiwi")

    elif (type == ("legume") and saison == ("ete")):
        print ("artichaut, aubergine, navet")

saison("fruits","ete")






