# Schleifenvariable (Bzw. Zählvariable): i, j, k
#Einleitung:
# counter = 10
# while counter >= 0:
    #counter = counter - 1 #alt.: counter -= 1
    #print(counter)
#Reihenfolge ist wichtig, ob zuerst print Befehl oder Counter
#----------------------------------------------------------------
#Addieren Sie in einer Schleife die Zahlen von 1 bis 100 und geben Sie das Ergebnis aus
summe = 0
counter = 0

while counter < 100:
    counter += 1
    print(counter)
    summe += counter
print("Summe:", summe)

    
    

