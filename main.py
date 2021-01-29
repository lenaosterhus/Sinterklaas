from sinterklaas import Sinterklaas
from datetime import datetime
from getpass import unix_getpass


def main():
    aaretsFilNavn = input("Årets txt-fil med gjester: ")
    historikkFilNavn = input('Historikkfil: ')
    aar = datetime.now().year

    sint = Sinterklaas(aar, aaretsFilNavn, historikkFilNavn)
    sint.skrivUtOversikt()
    
    # Bruker kan godkjenne oversikten før den lagres til historikk!
    godkjent = input("Ser dette greit ut? [y/n]): ")
    print()
    
    if (godkjent.lower() == "y"):
        sint.oppdaterHistorikk()
        sint.skrivHistorikkTilFil("historikk" + str(aar) + ".txt")
    else:
        print("Kjør programmet på nytt for å prøve igjen.")
        return

    # Info til epost
    login = input('Oppgi brukernavn (gmail): ')
    passord = unix_getpass(prompt='Oppgi passord (gmail): ')
    gavebelop = input('Oppgi gavebeløp: ')
    dato = input('Oppgi dato (eks. December 3rd): ')
    kontakt = input('Oppgi kontaktperson: ')

    sint.sendemail(login + '@gmail.com', login, passord, gavebelop, dato, kontakt)


main()
