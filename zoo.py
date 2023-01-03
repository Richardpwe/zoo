import konstanten


class Zoo(object):
    def __init__(self, name: str, strasse, hausnummer, plz, ort, eroeffnungsdatum, tierarten=[],
                 tiere=[], personal=[], futter=[]):
        self.name = name
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.plz = plz
        self.ort = ort
        self.eroeffnungsdatum = eroeffnungsdatum
        self.tierarten = tierarten
        self.tiere = tiere
        self.personal = personal
        self.futter = futter

    def get_futter_namen(self):
        futter_namen = []
        for futter in self.futter:
            futter_namen.append(futter.name)
        return futter_namen

    def get_tierarten_namen(self):
        tierarten_namen = []
        for tierart in self.tierarten:
            tierarten_namen.append(tierart.name)
        return tierarten_namen

    def get_tiere(self):
        return self.tiere

    def __str__(self):
        return 'ZOO: ' + self.name + '\nAdresse: ' + self.strasse + ' ' + str(self.hausnummer) + ', ' + \
            str(self.plz) + ' ' + self.ort + '\nEröffnet am: ' + str(self.eroeffnungsdatum)


class Personal(object):
    def __init__(self, name, anrede, geburtsdatum, strasse, hausnummer, plz, ort,
                 berufsbezeichnung, personalnummer, telefonnummer, gehalt):
        self.name = name
        self.anrede = anrede
        self.geburtsdatum = geburtsdatum
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.plz = plz
        self.ort = ort
        self.berufsbezeichnung = berufsbezeichnung
        self.personalnummer = personalnummer
        self.telefonnummer = telefonnummer
        self.gehalt = gehalt


class Tierpfleger(Personal):
    def __init__(self, name, anrede, geburtsdatum, strasse, hausnummer, plz,
                 berufsbezeichnung, personalnummer, telefonnummer, gehalt, tierart):
        Personal.__init__(name, anrede, geburtsdatum, strasse, hausnummer, plz,
                          berufsbezeichnung, personalnummer, telefonnummer, gehalt)
        self.tierart = tierart


class Tierart(object):
    def __init__(self, artname, tierklasse, futter):
        self.artname = artname
        self.tierklasse = tierklasse
        self.futter = futter


class Tier(Tierart):
    def __init__(self, artname, tierklasse, futter, name, geburtsdatum, geschlecht):
        Tierart.__init__(artname, tierklasse, futter)
        self.name = name
        self.geburtsdatum = geburtsdatum
        self.geschlecht = geschlecht


class Futter(object):
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis


neuer_zoo = Zoo("name", "strasse", 1, 22222, "ort", "eroeffnungsdatum", [], [], [])
