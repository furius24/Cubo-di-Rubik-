from typing import NewType, Tuple

# Creazione nuova tipologia di variabili di tipo Colore in formato RGB
Colore = NewType("Colore", Tuple[int, int, int])

# Creazione di istanze di tipo colore in formato RGB
WHITE = Colore((255, 255, 255))
GREEN = Colore((0, 255, 0))
ORANGE = Colore((255, 165, 0))
YELLOW = Colore((255, 255, 0))
BLUE = Colore((0, 0, 255))
RED = Colore((255, 0, 0))

# Realizzazione di una mappa di colori che associa a ogni faccia un colore
# Le singole configurazioni Up Front Left Back Right Down hanno un colore rappresentante la faccia del cubo di Rubik
MAPPA_COLORI_FACCE = [("U", WHITE), ("F", GREEN), ("L", ORANGE), 
                               ("B", BLUE), ("R", RED), ("D", YELLOW)]