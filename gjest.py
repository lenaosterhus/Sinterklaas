class Gjest:
    def __init__(self, navn, email):
        self._navn = navn
        self._email = email
        self._utvalgt = None

    # Legg til gjestens utvalgte (den gjesten skal skrive dikt om)
    def leggTilUtvalgt(self, person):
        self._utvalgt = person

    def hentNavn(self):
        return self._navn

    def hentEmail(self):
        return self._email

    def hentUtvalgt(self):
        return self._utvalgt

    def __str__(self):
        return self._navn + " will be writing a poem to " + self._utvalgt.hentNavn()
