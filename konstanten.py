import os

DARK_MODE = False
DARK_MODE_COLOR = "#777777"
TIERKLASSEN = ["Säugetier", "Vogel", "Reptil", "Amphib", "Fisch", "Muschel", "Spinnentier", "Insekt"]
TIERGESCHLECHTER = ["Männlich", "Weiblich", "Unbekannt"]

# Dateipfade Tiere
PLATZHALTER_BILD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-square.png')

ZOO_LOGO_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-zoo-2965351.png')

BEAR_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-bear-1866942.png')
BUTTERFLY_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-butterfly-1866908.png')
CAMEL_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-camel-1866909.png')
CAT_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-cat-1866911.png')
COW_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-cow-1866910.png')
CRAB_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-crab-1866912.png')
CROCODILE_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-crocodile-1866913.png')
DEER_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-deer-1866915.png')
DOG_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-dog-1866922.png')
ELEPHANT_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-elephant-1866916.png')
FLAMINGO_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-flamingo-1866938.png')
FOX_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-fox-1866920.png')
GIRAFFE_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-giraffe-1866914.png')
GOOSE_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-goose-1866923.png')
HEN_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-hen-1866919.png')
HORSE_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-horse-1866917.png')
KANGAROO_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-kangaroo-1866921.png')
KOALA_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-koala-1866918.png')
LION_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-lion-1866930.png')
MONKEY_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-monkey-1866924.png')
MOUSE_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-mouse-1866926.png')
OSTRICH_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-ostrich-1866925.png')
OWL_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-owl-1866927.png')
PENGUIN_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-penguin-1866931.png')
PIG_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-pig-1866940.png')
RABBIT_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-rabbit-1866933.png')
RHINOCEROS_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-rhinoceros-1866928.png')
SHARK_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-shark-1866939.png')
SHEEP_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-sheep-1866935.png')
SNAKE_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-snake-1866936.png')
SQUID_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-squid-1866932.png')
TIGER_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-tiger-1866929.png')
TURTLE_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-turtle-1866934.png')
WHALE_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-whale-1866937.png')
ZEBRA_PFAD = os.path.join(os.path.dirname(__file__), 'icons', 'noun-zebra-1866941.png')

TIERFOTOS = {
    "bear": BEAR_PFAD,
    "butterfly": BUTTERFLY_PFAD,
    "camel": CAMEL_PFAD,
    "cat": CAT_PFAD,
    "cow": COW_PFAD,
    "crab": CRAB_PFAD,
    "crocodile": CROCODILE_PFAD,
    "deer": DEER_PFAD,
    "dog": DOG_PFAD,
    "elephant": ELEPHANT_PFAD,
    "flamingo": FLAMINGO_PFAD,
    "fox": FOX_PFAD,
    "giraffe": GIRAFFE_PFAD,
    "goose": GOOSE_PFAD,
    "hen": HEN_PFAD,
    "horse": HORSE_PFAD,
    "kangaroo": KANGAROO_PFAD,
    "koala": KOALA_PFAD,
    "lion": LION_PFAD,
    "monkey": MONKEY_PFAD,
    "mouse": MOUSE_PFAD,
    "ostrich": OSTRICH_PFAD,
    "owl": OWL_PFAD,
    "penguin": PENGUIN_PFAD,
    "pig": PIG_PFAD,
    "rabbit": RABBIT_PFAD,
    "rhinoceros": RHINOCEROS_PFAD,
    "shark": SHARK_PFAD,
    "sheep": SHEEP_PFAD,
    "snake": SNAKE_PFAD,
    "squid": SQUID_PFAD,
    "tiger": TIGER_PFAD,
    "turtle": TURTLE_PFAD,
    "whale": WHALE_PFAD,
    "zebra": ZEBRA_PFAD
}
