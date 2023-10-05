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