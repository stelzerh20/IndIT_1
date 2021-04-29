# Aufgabe 1
# Schreiben Sie ein Python-Programm, das
# 1) den Benutzer begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Differenz der kleineren von der größeren Zahl berechnen
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotient der kleineren Zahl durch die größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)

print("Guten Tag, werter User!")
zahl1_string = input("Bitte geben Sie hier die erste Zahl ein:")
zahl2_string = input ("Bitte geben Sie hier die zweite Zahl ein:")

zahl1 = int(zahl1_string) #in Integer umwandeln, da sonst nicht rechenbar; bei Eingabe von Dezimalzahlen statt "int" den "float" nehmen
zahl2 = int(zahl2_string)

# Berechnung Addition
print("Die Addition ergab:", float(zahl1+zahl2)) #float Befehl ist für Nachkommastellen, sonst werden nur ganze Zahlen ausgegeben

# Differenz
if zahl2 > zahl1:#wenn zahl 2 größer als zahl 1 ist, wird zahl 1 von zahl 2 abgezogen
    print("Die Subtraktion ergab:", float(zahl2-zahl1))
    
elif zahl2 < zahl1:
    print("Die Subtraktion ergab: ", float(zahl1-zahl2)) #Wir gehen also davon aus, dass Zahl1 kleiner sein muss
    
else:
    print("Die Subtraktion ergab 1.0")

# Multiplikation
print("Die Multiplikation ergab:", float(zahl1*zahl2))

# Quotient

if zahl2 > zahl1:
    print("Die Division ergab:", float(zahl2/zahl1))
    
elif zahl2 < zahl1:
    print("Die Division ergab: ", float(zahl1/zahl2))
    
else:
    print("Die Division ergab 1.0")








