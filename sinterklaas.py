from gjest import Gjest
from math import factorial
import random
import smtplib

class Sinterklaas:
    def __init__(self, aar, navnefil, historikkfil):
        self._aar = aar
        self._gjester = []
        self._lesFil(navnefil)
        self._historikk = {} # Ordbok: Ingen objekter - bare navn
        self._lesHistorikk(historikkfil)
        self._velgUt()

        self._oppdaterHistorikk()
        self._skrivHistorikk("historikk" + str(self._aar) + ".txt")

    # Oppretter gjester og legger dem til i årets Sinterklaas
    def _lesFil(self, navnefil):
        with open(navnefil) as fildata:
            for linje in fildata:
                ord = linje.split(" <")
                navn = ord[0].strip("'")
                email = ord[1].rstrip(">;\n")
                gjest = Gjest(navn, email)
                self._gjester.append(gjest)


    def _lesHistorikk(self, histfilnavn):
        with open(histfilnavn) as fildata:
            for linje in fildata:
                navn = linje.strip().split(",")
                gjestNavn = navn.pop(0).strip()

                self._historikk[gjestNavn] = []
                for element in navn:
                    self._historikk[gjestNavn].append(element.strip())


    # Hver gjest får en utvalgt gjest å skrive dikt om. Den utvalgte kan ikke være gjesten selv.
    def _velgUt(self):
        utvalg = self._lagUtvalg()

        # print('Historikk:')
        # for gjest in self._historikk:
        #     print(gjest, ":", self._historikk[gjest])
        #
        # print('\nGjester:')
        # for gjest in self._gjester:
        #     print(gjest, end=' ')
        # print()
        #
        # print('\nUtvalg for feilsjekk:')
        # for utvalgt in utvalg:
        #     print(utvalgt, end=' ')
        # print()

        # Sjekker for feil helt til utvalget er godkjent eller at alle permutasjoner av utvalget er prøvd
        antFeil = 0
        while self._feilsjekkAlt(utvalg) == True:
            antFeil += 1

            # Hvis alle permutasjoner er prøvd --> finn en permutasjon som ikke "trekkes seg selv"
            if antFeil > factorial(len(utvalg)):
                while self._feilsjekkSegselv(utvalg) == True:
                    utvalg = self._lagUtvalg()
                break
            utvalg = self._lagUtvalg()

        #
        #     print('\nUtvalg etter feilsjekk:')
        #     for utvalgt in utvalg:
        #         print(utvalgt, end=' ')
        #     print()
        #     print("Antall feil:", antFeil)
        #
        # print("\nUtvalg OK.")

        for i in range(len(self._gjester)):
            self._gjester[i].leggTilUtvalgt(utvalg[i])


    # Kopierer gjestene over i en liste over tilgjenglige kandidater
    def _lagUtvalg(self):
        utvalg = []
        for gjest in self._gjester:
            utvalg.append(gjest)
        random.shuffle(utvalg)
        return utvalg

    # Sjekker om noen av gjestene har seg selv som utvalgt, eller om gjestene har hatt de utvalgte tidligere
    def _feilsjekkAlt(self, utvalg):
        for i in range(len(self._gjester)):
            if self._gjester[i] == utvalg[i]:
                return True
            # Hvis gjesten har historikk, sjekkes den utvalgte opp mot historikken
            elif self._gjester[i].hentNavn() in self._historikk:
                if utvalg[i].hentNavn() in self._historikk[ self._gjester[i].hentNavn() ]:
                    return True
        return False

    def _feilsjekkSegselv(self, utvalg):
        for i in range(len(self._gjester)):
            if self._gjester[i] == utvalg[i]:
                return True
        return False

    def _oppdaterHistorikk(self):
        for gjest in self._gjester:
            navn = gjest.hentNavn()
            if navn in self._historikk:
                self._historikk[navn].append(gjest.hentUtvalgt().hentNavn())
            else:
                self._historikk[navn] = [gjest.hentUtvalgt().hentNavn()]

    def _skrivHistorikk(self, histfilnavn):
        with open(histfilnavn, "w") as fildata:
            for navn in self._historikk:
                fildata.write(navn + "   ")
                for element in self._historikk[navn]:
                    fildata.write(", " + element)
                fildata.write("\n")


    # Skriver ut en oversikt over gjestenes navn
    def skrivUtOversikt(self):
        print("Sinterklaas " + str(self._aar) + ":")
        for gjest in self._gjester:
            print(gjest)
            print()


    def sendemail(self, from_addr, login, password, belop, dato):
        smtpserver = 'smtp.gmail.com:587'
        for gjest in self._gjester:

            navn = gjest.hentNavn()
            to_addr = gjest.hentEmail()
            utvalgt = gjest.hentUtvalgt().hentNavn()

            print("Starter sending for " + navn)
            print("Epost: " + to_addr)

            header = "From: %s\n" % from_addr
            header += "To: %s\n" % to_addr
            header += "Cc: lena.osterhus@gmail.com\n"
            header += "Subject: Sinterklaas " + str(self._aar) + "\n\n"

            message = "Dear " + navn + ",\n\n" + "The Sint is pleased to announce that for this year's Sinterklaas Eve lottery you have received " + utvalgt + " to write a poem and buy a " + belop + " NOK present for. On " + dato + " we will have a bag at the front door of our house in which you can put your present with the poem attached on top and the name of the person you have written it for visible on the outside. Remember to keep your name secret for everyone around you!\n\n" + "Any questions on how Sinterklaas works, please contact Stijn.\nWe are looking forward to a fun night,\n\n" + "Sint and Piet"

            message = header + message

            server = smtplib.SMTP(smtpserver)
            server.starttls()
            server.login(login, password)
            problems = server.sendmail(from_addr, to_addr, message)
            server.quit()

            print("Avslutter sending for " + navn)
            print()

            # return problems
