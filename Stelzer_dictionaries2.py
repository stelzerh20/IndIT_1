# Dictionaries
woerterbuch = {"Apfel": "apple",
               "Birne": "pear"}
try:
    print(woerterbuch[input("Begriff: ")]) # nur KeyError
except:
    print("Wort existiert nicht")

while True: # EIngabe bis Zahl eingegeben wurde
    try:
        stringA = input("Zahl: ")
        intb= int(stringA) # Umwanldung String to Int => nur ValueError möglich
        break
    except ValueError:
        print("ist keine Zahl")
print("ausgebrochen")