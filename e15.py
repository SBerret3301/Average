#algorithme note
#variable 
#       n1 , n2 , n3 , m : reel
#                 f : chaine de caracter
#Debut
#     Ecrire("tapez la 1 er note : ")
#     Lire(n1)
#     Ecrire("tapez la 2 eme note : ")
#     Lire(n2)
#     Ecrire("tapez la 3 eme note : ")
#     Lire(n3)
#     m= (n1 + n2 + n3)/3
#     tant que n1 > 20 ou n1 < 0 faire
#         Ecrire("tapez correctement la 1 er note : ")
#         Lire(n1)
#     fin tant que
#     tant que n2 > 20 ou n2 < 0 faire
#         Ecrire("tapez correctement la 2 eme note : ")
#         Lire(n2)
#     fin tant que
#     tant que n3 > 20 ou n3 < 0 faire
#         Ecrire("tapez correctement la 3 eme note : ")
#         Lire(n3)
#     fin tant que
#     si m >= 16 alors
#        f <-- "tres bien"
#     sinon
#         si m < 16 et m >= 14 alors
#            f <-- "bien"
#         sinon
#             si m < 14 et m >= 12 alors
#                f <-- "assez bien"
#             sinon
#                 si m < 12 et m >= 10 alore
#                    f <-- "passable"
#                 sinon
#                     si m < 10 alors
#                         f <-- "insuffisant"
#                     fin_si
#                 fin_si
#             fin_si
#         fin_si
#     fin_si
#     Ecrire("la moyenne est : ",m,"il est : ",f)








n1 = float(input("enter the first mark : "))
n2 = float(input("enter the second mark : "))
n3 = float(input("enter the third mark : "))
while n1 > 20 or n1 <0 :
    n1 = float(input("Enter the first mark correctly  : "))
while n2 > 20 or n2 < 0 :
    n2 = float(input("Enter the second mark correctly : "))
while n3 > 20 or n3 < 0 :
    n3 = float(input("Enter the third mark correctly : "))
m = (n1 + n2 + n3)/3
if m >= 16 :
    f = "very good"
elif m >= 14 and m < 16 :
    f = "Good"
elif m >= 12 and m < 14 :
    f = "it's OK"
elif m >= 10 and m < 12 :
    f ="acceptable"
else :
    f="insufficient"
print("the average is : ", m ,"it's ",f)