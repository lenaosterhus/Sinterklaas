# Sinterklaas
## Hva er Sinterklaas?
Sinterklaas er den nederlandske versjonen av Sankt Nikolas (Sint-Nicolaas på nederlandsk) som feires 5.-6. desember, og er en festdag for både troende og ikke-troende, gamle og unge.

En uke eller to før sinterklaaskvelden kommer, er det på skoler og i familier ikke uvanlig at man skriver alle klassens / familiens navn på lapper, og trekker den man skal gi en gave («surprise») og et dikt til.

Om kvelden 5. desember åpnes gavene, etter at man har lest diktet høyt og prøvd å gjette hva det er i pakken og hvem som har gitt den.

## Hvorfor dette skriptet?
Hvert år får jeg i oppgave å trekke disse lappene for min mor og Nederlandske stefars feiring med venner. I 2018, med IN1000 Introduksjon til objektorientert programmering på UiO i bagasjen, fant jeg ut at kanskje det var enklere å lage et skript som kunne gjøre jobben for meg. 

## Trekning
Hver gjest får en utvalgt gjest å skrive dikt om. Kriterier: 1. Den utvalgte kan ikke være gjesten selv, og 2. skal helst ikke være en gjesten har hatt som utvalgt før.

Skriptet sjekker for disse kriteriene helt til utvalget er godkjent, eller at alle permutasjoner av utvalget er prøvd. Hvis alle permutasjoner er prøvd brukes et utvalg som bare holder for kriterie 1.

## .txt-filer
Skriptet forutsetter at man har to txt-filer i samme mappe som scriptet kjøres fra.

1. En txt-fil med årets gjester på egne linjer, på følgende format:
```
'Gjest 1' <gjest1@gmail.com>;
'Gjest 2' <gjest2@hotmail.com>;
```
2. En .txt-fil med historikk for gjestene, på følgende format:
```
fra,        til, til, til, ...
Gjest 0,    Gjest 3, Gjest 1
Gjest 1,    Gjest 2, Gjest 0
Gjest 2,    Gjest 1
```

## E-post
E-posten sendes ut fra oppgitt brukernavn (gmail) med avsender på kopi. 

**OBS!** Google-kontoen må ha gitt tilgang til mindre sikre apper (https://myaccount.google.com/lesssecureapps).

Teksten som sendes ut:

> Dear [navn mottaker],
>
> The Sint is pleased to announce that for this year's Sinterklaas Eve lottery you have received [navn utvalgt] to write a poem and buy a [beløp] NOK present for. 
>
> On [dato] we will have a bag at the front door of our house in which you can put your present with the poem attached on top and the name of the person you have written it for visible on the outside. Remember to keep your name secret for everyone around you!
> 
> Any questions on how Sinterklaas works, please contact [kontaktperson]. 
> We are looking forward to a fun night, 
>
> Sint and Piet"

## Kjøring

```
python3 main.py
```
Eksempel på kjøring:
```
python3 main.py
Årets txt-fil med gjester: test.txt
Historikkfil: testHistorikk.txt

--- SINTERKLAAS 2021---
Gjest 1 will be writing a poem to Gjest 3
Gjest 4 will be writing a poem to Gjest 2
Gjest 2 will be writing a poem to Gjest 4
Gjest 3 will be writing a poem to Gjest 1

Ser dette greit ut? [y/n]): y

Historikk skrives til fil historikk2021.txt

Oppgi brukernavn (gmail): ....
Oppgi passord (gmail): ....
Oppgi gavebeløp: 200
Oppgi dato (eks. December 3rd): December 3rd
Oppgi kontaktperson: Lena

Starter sending for Gjest 1
Epost: gjest1@gmail.com
Avslutter sending for Gjest 1
...

```