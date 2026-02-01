import random
lettre =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chiffre = ["0","1","2","3","4","5","6","7","8","9"]
caractère_spéciaux =["~","#","}","{","[","|","`","^","@","]","?",".","/","§",",",";",":","!","%","£","*","+","."]
nbrcar = 0
caractère_chiffre=0
caractère_spécio=0
mot_de_passe = ""

nbrcar = int(input("entrez le nombre de caractères minimum souhaitez:"))
caractère_chiffre = input("voulez vous des chiffres ?:o/n:").lower()
caractère_spécio = input("voulez vous des caractères spéciaux ?:o/n:").lower()

for i in range(nbrcar) :
   mot_de_passe += lettre[random.randint(0,len(lettre)-1)]

if caractère_chiffre == "o" or caractère_chiffre =="yes" or caractère_chiffre =="oui":
    for i in range(random.randint(1, 5)):
     mot_de_passe += chiffre[random.randint(0,len(chiffre)-1)]

if caractère_spécio == "o" or caractère_spécio  == "yes" or caractère_spécio== "oui":
    for i in range(random.randint(1, 5)):
     mot_de_passe += caractère_spéciaux[random.randint(0,len(caractère_spéciaux)-1)]


print(mot_de_passe)






