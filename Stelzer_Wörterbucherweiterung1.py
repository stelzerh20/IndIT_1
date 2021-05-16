# 2) Liste
#a) Eingabe Suchbegriff (deutsch)
#b) Bestimmung der Gesamtzahl der Elemente (=maximaler Index)
#c) Schleife: vergleich Eingabe mit jew. Listenelement
#d) Wenn Element gefunden -> Index speichern
#e) Zugriff auf Listenelement [Index] in Liste (englisches Wörterbuch)
#Beispiel:
print("Guten Tag, dies ist der Google-Translator")
#meine_Liste = ["Ich bin", "ein", "string in einer", "liste"]
#print(meine_Liste[2]) # 2. Element ist jetzt das Element ´string in einer´
woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]


#-----------------------------------------------------------------------------
# Erweitern Sie das Wörterbuch-Beispiel um die Möglichkeit, Einträge zu ergänzen bzw. zu löschen
# ENGLISCH VERSION WURDE NOCH NICHT GEMACHT - GEHT NUR AUF DEUTSCH
auswahl = input("Welchen Befehl möchten Sie ausführen? [E]infügen, [L]öschen, [A]bfragen?")
if auswahl == "E" or auswahl == "e":
#Einfügen
    einfuegen = input("Welchen Eintrag möchten Sie hinzufügen?")
    woerterbuch_deutsch.append(einfuegen)
    print("Der folgende Eintrag wurde gemacht:", einfuegen)
    print("Das Wörterbuch enthält nun folgende Einträge:", woerterbuch_deutsch)

elif auswahl == "L" or auswahl == "l":
#Löschen
    
    loeschen = input("Welchen Eintrag möchten Sie löschen?")
    woerterbuch_deutsch.remove(loeschen)
    print("Der folgende Eintrag wurde gelöscht:", loeschen)
    print("Das Wörterbuch enthält nun folgende Einträge: ", woerterbuch_deutsch)

else: #Standardvorgang -> immer mit dem geringsten Risiko
#Abfrage
#------------------------------------------------------------------------------
#Von Deutsch auf Englisch übersetzen:
    uebersetzen = input("Bitte geben Sie hier das zu übersetzende Wort ein:")
    Index_Wort = 0 #Man startet immer mit 0, wobei jeder Index einem Wort zugeordnet ist
    Laufvariable = len(woerterbuch_deutsch) or len(woerterbuch_english) #Hier wird festgelegt, dass die Laufvariable die Anzahl der Elemente der Wörterbücher ist
    k = 0 #k benötigt man für die While-Schleife, um dem Programm zu sagen, wann es stoppen soll
    while k < Laufvariable:
            
        if woerterbuch_deutsch[k].lower() == uebersetzen.lower(): #lower, damit Groß- und Kleinschreibung egalisiert werden
            Index_Wort = k
            print("Die Übersetzung ins Englische lautet:", woerterbuch_english[Index_Wort],"(EN)") #Hier wird die Übersetzung mit dem Hinweis auf die Sprache ausgegeben (EN)
            break # Wenn die obrige Bedingung erfüllt wird, bewirkt ´break´, dass die Schleife damit verlassen wird
        k += 1 # k soll immer um 1 erhöht werden
       
    
       # Wenn die Anzahl der Schleifen erreicht ist, in denen sich Wörterbucheinträge befinden, soll das Programm einen Fehler ausgeben
        if k == Laufvariable:
            print ("Dieses Wort existiert nicht")
      
      
        elif woerterbuch_english[k].lower() == uebersetzen.lower():
            Index_Wort = k
            print("Die Übersetzung ins Deutsche lautet:", woerterbuch_deutsch[Index_Wort],"(DE)")
            break
      
#-----------------------------------------------------------------------
