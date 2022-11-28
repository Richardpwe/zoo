class Zoo(object):
    def __init__(self, name, strasse, hausnummer, plz, ort, eröffnungsdatum):
        self,name = name
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.plz = plz
        self.ort = ort
        self.eröffnungsdatum = eröffnungsdatum

class Personal(object):
    def __init__(self, name, anrede, geburtsdatum, strasse, hausnummer, plz, ort, berufsbezeichnung, personalnummer, telefonnummer, gehalt):
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
    def __init__(self, name, anrede, geburtsdatum, strasse, hausnummer, plz, berufsbezeichnung, personalnummer, telefonnummer, gehalt, tierart):
        Personal.__init__(name, anrede, geburtsdatum, strasse, hausnummer, plz, berufsbezeichnung, personalnummer, telefonnummer, gehalt)
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