a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if a <= 0 or b <= 0 or c <= 0:
 print("Les longueurs doivent être positives.")

elif a + b <= c or a + c <= b or b + c <= a:
 print("Ce triangle est impossible.")

else:
 print("Le triangle est possible.")

if a == b == c:
 print("Le triangle est équilatéral.")
elif a == b or a == c or b == c:
 print("Le triangle est isocèle.")
else:
 print("Le triangle est quelconque.")

if (a*a + b*b == c*c or
a*a + c*c == b*b or
b*b + c*c == a*a):
 print("Le triangle est rectangle.")