#ungarische Notation:
#strZahl_1 = input("erste Zahl: ") #Nummerierung angewöhnen
#IntZahl_1 = int(strZahl_1)

#--------------------------------------------------------------

#26.03.2021

#Einfaches '=' Zeichen: Zuweisung

strWetter = input("Wochenendwetter - 'sonnig' oder 'regnerisch'")

#Doppeltes '==' Zeichen: Vergleichsoperator ; siehe w3schools.com

#Gartenparty:
if strWetter == "sonnig":
    print("Gartenparty")
elif strWetter == "regnerisch":#oder wenn - Doppelpunkte nicht vergessen!
    print("Kellerparty")
else:
    print("bitte entweder 'sonnig' oder 'regnerisch' eingeben!")

#Einrückungen: Für Reihenfolge der Aktionen verantwortlich; wenn man eine Aktion nicht einrückt, wird diese IMMER ausgeführt, egal was oben steht
# z.B. nach dem Print-Befehl

#Kellerparty Alternativen
#if strWetter != "sonnig": # '!=' bedeutet 'not'
   # print("Kellerparty")

#if strWetter == "regnerisch":
    #print("Kellerparty")
   
   
#Debugger starten (siehe Menüleiste) F5
#Große Schritte: STRG F6
#Kleine Schritte: STRG F7
   
   
   
   
   
   
   
   