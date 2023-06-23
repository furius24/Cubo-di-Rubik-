from typing import NewType, Dict, Literal

from .colore import Colore

# Creazione di due variabili del tutto nuove utili alla gestione di angoli e bordi del cubo
Angolo = NewType("Angolo", Dict[str, Colore])
Bordo = NewType("Bordo", Dict[str, Colore])

# Creazione di un dizionario di conversione utile a convertire i singoli bordi
# Per esattezza i dizionari forniscono una mappatura dei pezzi del cubo
# a sequenze di movimenti che possono essere eseguiti per raggiungere una determinata configurazione
# Questo può tornare poi utile alla identificazione e alla soluzione
BORDO_A_UF = {
    "UF": "U2 U2",
    "UL": "U'",
    "UR": "U",
    "UB": "U2",
    "LB": "L2 F",
    "LD": "L' F",
    "LF": "F",
    "RB": "R2 F'",
    "RD": "R F'",
    "RF": "F'",
    "DB": "D2 F2",
    "DF": "F2"
}

# Creazione di un dizionario di conversione utile a convertire i singoli angoli
ANGOLO_A_UFR = {
    "UFR": "U2 U2",
    "DFR": "R",
    "DBR": "R2",
    "URB": "U",
    "ULF": "U'",
    "UBL": "U2",
    "DFL": "L' U'",
    "DBL": "L2 U'"
}
