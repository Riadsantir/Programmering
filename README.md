# Programmering
Loggbok 
=========================

23 09 21 
----------------
Gjorde:
### 7070 slumptal
Fil: 7070 slumptal.py

Exempel:

import random

saldo = 0

print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("två lika - 3 kr")
print("en sexa - 5 kr")
print("stege - 1 kr")

while True:
    val = input("Välj spela (s), sätt in pengar (i), eller avsluta (a): ")

    if val == 'a':
        print("Vad roligt att du spelade en stund!")
        break
    elif val == 'i':
        insattning = int(input("Ange belopp att sätta in: "))
        saldo += insattning
        print(f"Att spela för: {saldo}")
    elif val == 's':
        if saldo < 1:
            print("Du har inte tillräckligt med pengar.")
        else:
            saldo -= 1
            tarning1 = random.randint(1, 6)
            tarning2 = random.randint(1, 6)

            print(tarning1, tarning2)

            if tarning1 == 6 or tarning2 == 6:
                print("sex-vinst + 5kr")
                saldo += 5
            elif tarning1 == tarning2:
                print("två lika + 3 kr")
                saldo += 3
            elif (tarning1 == 1 and tarning2 == 2) or (tarning1 == 2 and tarning2 == 1):
                print("steg-vinst + 1kr")
                saldo += 1
            else:
                print("förlust")

            print(f"Att spela för: {saldo}")

Gick riktigt bra.
Jag har lärt mig många olika saker denna gången, har lärt mig skillnaden mellan vanligt print() och print(f "" ). Att importera random är också en ny sak för mig, men det
väldigt enkelt. Att använda variabel och ge den ett värde som kan ändras på grund av outputen är också väldigt spännande, som i den här gången var {saldo}. 


vecka 39-40
--------------
gjorde 
### 7073 flödesdiagram 
Fil: 7073 flödesdiagram.py

jag kan inte klistra in flödesdiagram här, men koden har jag skrivit. 
exempel :

~~~

'''
tal = int(input("Mata in ett tal: "))

if tal < 0:
    print("Tal mindre än 0 är negativa.")
elif 0 <= tal <= 9:
    print("Det är ensiffriga tal.")
elif 10 <= tal <= 99:
    print("Det är tvåsiffriga tal.")
elif 100 <= tal <= 999:
    print("Det är tresiffriga tal.")
else:
    print("Det är minst fyrsiffriga tal.")
'''
'''
gissning = int(input("Gissa ett tal: "))
while gissning != 4:
    print("Du gissade fel. Gissa på ett annat tal.")
    gissning = int(input("Gissa ett tal: "))
print("Du gissade rätt.")
'''
'''
tal = int(input("Ange ett tal: "))
antal_gissningar = 0
while tal != 42:
    antal_gissningar += 1
    if tal < 42:
        print("För litet")
    elif tal > 42:
        print("För stort")
    tal = int(input("Ange ett tal: "))
print(f"Du behövde {antal_gissningar} gissningar för att hitta rätt svar.")
'''
import random

def sten_sax_pase():
    spelare = input("Välj sten, sax eller påse: ").lower()
    datorn = random.choice(["sten", "sax", "påse"])

    print(f"Datorn valde: {datorn}")

    if spelare == datorn:
        print("Oavgjort!")
    elif spelare == "sten":
        if datorn == "sax":
            print("Spelaren vinner!")
        else:
            print("Datorn vinner!")
    elif spelare == "sax":
        if datorn == "sten":
            print("Datorn vinner!")
        else:
            print("Spelaren vinner!")
    elif spelare == "påse":
        if datorn == "sten":
            print("Spelaren vinner!")
        else:
            print("Datorn vinner!")
    else:
        print("Ogiltigt val. Försök igen.")

while True:
    sten_sax_pase()
    fortsatt = input("Vill du spela igen? (ja/nej): ").lower()
    if fortsatt != "ja":
        break

print("Tack för att du spelade!!")

~~~

Gick riktigt bra.
Har rittat olika flödesdiagram till alla kod som ligger där uppe, ganska enkelt att göra så och man ska använda det innan man börja programmera något projekt, så skulle jag göra i alla fall. While True och att definera, som i detta fall def sten_sax_pase(): är något nytt som jag har lärt mig, .lower också men det var ganska enkelt. 

Vecka 41-42 
----------------
Gjorde:
### 7100 listor
Fil: 7100 listor.py

Exempel:

~~~
import random

# Kasta en sexsidig tärning 10 gånger och spara resultaten i en lista
resultat_lista = [random.randint(1, 6) for _ in range(10)]
resultat_lista.sort()
summa = sum(resultat_lista)
medelvärde = summa / len(resultat_lista)
minsta = min(resultat_lista)
största = max(resultat_lista)
antalet_sexor = resultat_lista.count(6)
vanligaste_valören = max(set(resultat_lista), key = resultat_lista.count)

# Skriv ut resultaten
print("Resultat:", resultat_lista)
print("Sorterat:", resultat_lista)
print("Summa:", summa)
print("Medelvärde:", medelvärde)
print("Minsta:", minsta)
print("Största:", största)
print("Antal sexor:", antalet_sexor)
print("Vanligast:", vanligaste_valören)

~~~

Jag har lärt mig hur man kan använda listor i Python för att spara och hantera resultat. Listor var mycket storre och bredare än vad jag trode innan jag börjar jobba med dem, de kan exempelvis användas för att samla data, som i det här fallet de olika tärningskasten. Jag har även lärt mig hur man kan använda loopar, som en for-loop, för att upprepa en handling flera gånger. I det här exemplet har jag använt en lista för att spara resultaten av tärningskasten, sedan sorterades listan och beräknades summan och medelvärdet.

Vecka 43-45
----------------
Gjorde:
### 7100 listor ( 7100 A och B 5 yatzy )
Fil: 7100 A 5 yatzy
     7100 B 5 yatzy

Exempel:

~~~

import random
def kasta_tärning():
    return random.randint(1, 6)
tärningskast = [kasta_tärning() for _ in range(5)]
if all(tärning == tärningskast[0] for tärning in tärningskast):
    print("Yatzy")
else:
    print("Inte Yatzy")


~~~

~~~
import random

def kasta_tärning():
    return random.randint(1, 6)
tärningskast = [kasta_tärning() for _ in range(5)]
antalet_ettor = tärningskast.count(1)
print(f"Antalet ettor är: {antalet_ettor}")

~~~

Jag har lärt mig hur man använder listor och loopar i Python för att hantera data och utföra olika operationer.
Exempelvis hur man skapar och manipulerar listor i Python för att organisera och analysera data. Jag har även sett hur man kan använda loopar och villkor för att utföra olika åtgärder baserat på data i listor. Jag försökte också att lärt mig att skapa och använda funktioner för att göra koden mer strukturerad och återanvändbar. 

Ingenting var svårt denna gången, det var enklare än förra uppgiften (Primtal uppgift)

Vecka 44
----------------
Gjorde:
höstlov.

Vecka 45
----------------
Gjorde:
### 7100 listor ( 7100 A och B 5 yatzy )
Fil: 7100 A 5 yatzy
     7100 B 5 yatzy

Exempel: ligger ovan i vecka 43. 

Vecka 46
----------------
Gjorde:
### har gjort alla prov som jag missade/gick dåligt. 

Exempel: ingen exempel, jag har tränat på gamla exempel och testade små koder som behöver inte nämnas, bara för att memorera allt inför provet. Jag löste alla exempeltest som Rikard har lagt ut så att jag förstå hur ungefär provet kommer att se ut. 

Vecka 47
----------------
Gjorde:
### 7080 definiera funktioner (bara som en test för att förstå hur koden fungerar)

Jag började med att definera funktioner på måndagen. Jag skrev ingen unik kod. På torsdagen hade Jag resursdag hela dagen. 

Vecka 48
----------------
Gjorde:
### klarade alla test 

på måndagen så repeterade jag allt som vi gick igenom, fokuserade mest på att definiera funktioner. Att kunna läsa och förstå def funktioner hade jag nästan inga problem alls. Men att definera funktioner själv var lite jobbigt så jag jobbade med det nästan hela lektionen. På torsdagen så gjorde jag alla test som var kvar och klarade alla, jag skrev i loggboken under lektionen också. Jag installerade VSCodium på min ny dator som jag fick så jag kunde inte programmera under denna lektionen. 

Vecka 49
----------------
Gjorde:
### Började bestämma över projektet

på måndagen så bestämmde jag att jag ska göra en miniräknare som ett litet projekt för att jag tycker att det var intressant. Jag kollade på flera YouTube videor som visar tänkesätt när man ska skapa en miniräknare med hjälp av Python. 


Vecka 50
----------------
Gjorde:

~~~
function kastaTarning() {
    return Math.floor(Math.random() * 6) + 1;
}

let tarningskast;
do {
    tarningskast = Array.from({ length: 5 }, kastaTarning);
    if (tarningskast.every(tarning => tarning === tarningskast[0])) {
        console.log("Yatzy");
    } else {
        console.log("Inte Yatzy");
    }
} while (!tarningskast.every(tarning => tarning === tarningskast[0]));

~~~

Jag har lärt mig grunderna i JavaScript och hur man kan använda slumpmässiga tal och villkor för att skapa ett enkelt tärningsspel. I detta exempel så loppar koden till jag får Yatzy.

Vecka 2
----------------
Gjorde:

~~~
import random

def guess_number():
    number = random.randint(1, 100)
    guess = int(input("Gissa ett nummer mellan 1 och 100: "))
    if guess == number:
        print("Grattis, du har gissat rätt!")
    else:
        print(f"Tyvärr, det rätta numret var {number}.")

guess_number()
~~~

Jag har fortsatt lära mig grundläggande JavaScript genom att skapa ett enkelt nummergissningsspel. Fast där stuttade jag på massa nya saker och det fanns så många saker som inte fungerade för mig och då försökte jag att översätta den python kod som ligger övanför till javascript kod och jag kom på följande: 

~~~
function guessNumber() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const number = Math.floor(Math.random() * 100) + 1;

    rl.question('Gissa ett nummer mellan 1 och 100: ', (answer) => {
        const guess = parseInt(answer);
        if (guess === number) {
            console.log("Grattis, du har gissat rätt!");
        } else {
            console.log(`Tyvärr, det rätta numret var ${number}.`);
        }
        rl.close();
    });
}

guessNumber();

~~~
Denna koden funkar inte riktigt för mig heller, tog lite hjälp från ChatGPT och det hjälpte inte så myckte riktigt heller men försökte i alla fall. 


Vecka 3
----------------
Gjorde:

~~~
import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    length = 12
    password = "".join(random.sample(characters, length))
    return password

print("Genererat lösenord:", generate_password())
~~~

Jag har lärt mig att skapa slumpmässiga lösenord av olika längder med hjälp av JavaScript, men ändå började jag fokusera igen på python för att jag tycker att mitt projekt som jag vill göra kommer var skriven i Python, det känns svårt att hinna gör en bra medel-avancerad projekt med javascript.

Vecka 4
----------------
Gjorde:

~~~
import random

def shuffle_list(my_list):
    random.shuffle(my_list)
    return my_list

my_list = [1, 2, 3, 4, 5]
print("Blandad lista:", shuffle_list(my_list))
~~~

Jag har lärt mig att blanda ordningen på element i en lista med hjälp av random-modulen.

Vecka 5
----------------
Gjorde:

~~~
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.12', 5555))
s.send(b'Hello server!')
data = s.recv(1024)
print('Received:', data.decode())
s.close()
~~~

Jag har börjat utforska socket-programmering i Python och lärt mig att skicka och ta emot data över ett nätverk.

Vecka 6
----------------
Gjorde:

~~~
import os

file_path = '/home/user/Documents/example.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print("Filen har raderats.")
else:
    print("Filen finns inte.")

~~~

Jag har lärt mig att använda modulen `os` för att hantera filer och mappar i Python, inklusive att radera filer.

Vecka 8
----------------
Gjorde:

~~~
import subprocess

subprocess.run(['ls', '-l'])
~~~

Jag har börjat använda modulen `subprocess` för att köra externa kommandon och program från Python.

Vecka 9
----------------
Gjorde:

~~~
import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)
print(json_data)
~~~

Jag har lärt mig att konvertera Python-dictionaryn till JSON-format med hjälp av modulen `json`.

Vecka 10
----------------
Gjorde:

~~~
import time

print("Väntar i 5 sekunder...")
time.sleep(5)
print("Klart!")
~~~

Jag har lärt mig att använda modulen `time` för att skapa fördröjningar eller väntetider i Python-program.

OBS
--
Jag ska redigera vecka 5 och vecka 8 och kanske små andra saker från olika veckor, eller kanske lägga till massa andra saker som jag gjorde fast jag orkar inte skriva om. 

