from sinterklaas import Sinterklaas




def hovedprogram():
    aaretsFilNavn = input('Årets fil: ')
    historikkFilNavn = input('Historikkfil: ')

    sint2019 = Sinterklaas(2019, aaretsFilNavn, historikkFilNavn)
    sint2019.skrivUtOversikt()

    login = input('Oppgi brukernavn (gmail): ')
    passord = input('Oppgi passord (gmail): ')
    gavebelop = input('Oppgi gavebeløp: ')
    dato = input('Oppgi dato (eks. December 3rd): ')

    sint2019.sendemail('lena.osterhus@gmail.com', login, passord, gavebelop, dato)



hovedprogram()
