import os
import pickle
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

    def get_futter_by_name(self, futter_name):
        for futter in self.futter:
            name = futter.get_name()
            if name == futter_name:
                return futter

    def get_tierarten_namen(self):
        tierarten_namen = []
        for tierart in self.tierarten:
            tierarten_namen.append(tierart.artname)
        return tierarten_namen

    def get_tierart_by_name(self, tierart_name):
        for tierart in self.tierarten:
            name = tierart.get_artname()
            if name == tierart_name:
                return tierart

    def get_tiere(self):
        return self.tiere

    def get_tiere_by_name(self, tiername):
        for tier in self.tiere:
            name = tier.get_tiername()
            if name == tiername:
                return tier

    def tier_loeschen(self, zu_loeschen):
        for tier in self.tiere:
            if tier == zu_loeschen:
                index = self.tiere.index(tier)
                del self.tiere[index]

    def zoo_speichern(self):
        with open('zoo.pickle', 'wb') as zoo_datei:
            pickle.dump(self, zoo_datei)

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
    def __init__(self, bild, artname, tierklasse, futter):
        self.bild = bild
        self.artname = artname
        self.tierklasse = tierklasse
        self.futter = futter

    def get_artname(self):
        return self.artname

    def get_tierklasse(self):
        return self.tierklasse

    def get_futter(self):
        return self.futter

    def get_bild(self):
        return self.bild


class Tier(Tierart):
    def __init__(self, bild, artname, tierklasse, futter, name, geburtsdatum, geschlecht):
        super().__init__(bild, artname, tierklasse, futter)
        self.name = name
        self.geburtsdatum = geburtsdatum
        self.geschlecht = geschlecht

    def __init__(self, name, geburtsdatum, geschlecht, tierart):
        self.name = name
        self.geburtsdatum = geburtsdatum
        self.geschlecht = geschlecht
        self.bild = tierart.get_bild()
        self.artname = tierart.get_artname()
        self.tierklasse = tierart.get_tierklasse()
        self.futter = tierart.get_futter()
        self.tierart = tierart

    def get_tiername(self):
        name: str = self.name
        return name

    def get_geburtsdatum(self):
        return self.geburtsdatum

    def get_geschlecht(self):
        return self.geschlecht


class Futter(object):
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis

    def get_name(self):
        return self.name


file_path = 'zoo.pickle'
if os.path.exists(file_path):
    with open(file_path, 'rb') as datei:
        neuer_zoo = pickle.load(datei)
else:
    neuer_zoo = Zoo("name", "strasse", 1, 22222, "ort", "eroeffnungsdatum", [], [], [])
