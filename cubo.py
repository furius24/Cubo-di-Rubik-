from typing import List, TypeVar, Union

from itertools import permutations

from .movimenti import Movimenti
from .colore import Colore, MAPPA_COLORI_FACCE
from .pezzi import Angolo, Bordo, ANGOLO_A_UFR, BORDO_A_UF
from ..mischia import controllore

# Creazione della classe Cubo
class Cubo:
    # Metodo costruttore del cubo
    def __init__(self, dimensione: int):
        self.dimensione = dimensione
        self.facce = {faccia: self.genera_faccia(Colore, dimensione) 
                      for faccia, Colore in MAPPA_COLORI_FACCE}

    # Rileva colore dello sticker in esame
    def get_sticker(self, sticker: str) -> Colore:
        # Itero su ogni possibile permutazione dello sticker
        for perm in permutations(sticker):
            # Concateno e controllo se è presente nel dizionario dei bordi
            if "".join(perm) in BORDO_A_UF:
                # Ritorno le info relative
                return self.get_bordo("".join(perm))[sticker[0]]
            # Concateno e controllo se è presente nel dizionario degli angoli
            elif "".join(perm) in ANGOLO_A_UFR:
                # Ritorno le info relative
                return self.get_angolo("".join(perm))[sticker[0]]
        # In caso di errore invio eccezione
        raise ValueError(f"Sticker non valido: {sticker}")

    # Rileva bordo dal quadrato in esame
    def get_bordo(self, pezzo: str) -> Bordo:
        # Trasformo il bordo in un possibile movimento nel dizionario
        Movimenti = controllore.trasf_in_movimenti(BORDO_A_UF[pezzo])
        # Eseguo i movimenti per definirlo
        self.esegui_movimenti(Movimenti)
        # Compongo le informazioni sui colori del bordo
        info = Bordo({
            pezzo[0]: Colore(self.facce["U"][-1][1]),
            pezzo[1]: Colore(self.facce["F"][0][1])
        })
        # Inverto i movimenti
        controllore.inverti_movimenti(Movimenti)
        # Ritorno le informazioni sul bordo
        return info

    # Rileva angolo dall'angolo in esame
    def get_angolo(self, pezzo: str) -> Angolo:
        # Trasformo l'angolo in un possibile movimento nel dizionario
        Movimenti = controllore.trasf_in_movimenti(ANGOLO_A_UFR[pezzo])
        # Eseguo i movimenti riguardanti l'angolo
        self.esegui_movimenti(Movimenti)
        # Compongo le informazioni sui colori dell'angolo
        info = Angolo({
            pezzo[0]: Colore(self.facce["U"][-1][-1]), # Up
            pezzo[1]: Colore(self.facce["F"][0][-1]), # Front
            pezzo[2]: Colore(self.facce["R"][0][0]) # Right
        })
        # Inverto i movimenti eseguiti precedentemente
        controllore.inverti_movimenti(Movimenti)
        # Ritorno le info sull'angolo
        return info

    # Metodo per far eseguire i movimenti in una lista di movimenti al cubo
    def esegui_movimenti(self, Movimenti: Union[str, List[Movimenti]]):
        # Controllo sulla lista di movimenti
        if isinstance(Movimenti, str):
            Movimenti = controllore.trasf_in_movimenti(Movimenti)
        # Per ogni movimento controllo se è verticale o meno e lo eseguo
        for movimento in Movimenti:
            if movimento.faccia == "y":
                self.ruota_verticalmente()
            else:
                self.ruota(movimento)

    # Metodo per controllare se il cubo è risolto
    def e_risolto(self) -> bool:
        # Itero su ogni faccia
        for faccia in self.facce.values():
            for riga in faccia:
                # Controllo se un qualsiasi pezzo risulta diverso
                if any(pezzo_colore != faccia[0][0] for pezzo_colore in riga):
                    return False

        return True

    # Metodo per la generazione della singola faccia
    def genera_faccia(self, Colore: Colore, dimensione: int):
        # Ritorno la matrice corrispondente alla faccia
        return [[Colore for _ in range(dimensione)] for _ in range(dimensione)]

    # Metodo per ruotare una faccia in senso orario
    def ruota_faccia(self, faccia: str):
        # Inversione e trasposizione della faccia per fare avvenire la rotazione
        self.facce[faccia] = [list(riga) for riga in zip(*self.facce[faccia][::-1])]

    # Metodo per modificare le facce adiacenti
    def modifica_faccia_adiacente(self, faccia: str):
        # Se la faccia è quella superiore
        if faccia == "U":
            # Estraggo il primo elemento da ogni faccia
            l = [self.facce[faccia][0] for faccia in ["F", "L", "B", "R"]]
            # Shifto di una posizione 
            self.facce["F"][0], self.facce["L"][0], \
                self.facce["B"][0], self.facce["R"][0] = l[-1:] + l[:-1]
        # Se la faccia è quella inferiore
        elif faccia == "D":
            # Estraggo l'ultimo elemento da ogni faccia
            l = [self.facce[faccia][-1] for faccia in ["F", "L", "B", "R"]]
            # Shifto di una posizione
            self.facce["F"][-1], self.facce["L"][-1], \
                self.facce["B"][-1], self.facce["R"][-1] = l[1:] + l[:1]
        # Se la faccia è quella frontale
        elif faccia == "F":
            # Creo una lista 
            l = [self.facce["U"], trasposizione(self.facce["R"]),
                 self.facce["D"], trasposizione(self.facce["L"])]
            # Creo una lista degli angoli delle facce di l e li sposto
            r = [l[0][-1], l[1][0][::-1], l[2][0], l[3][-1][::-1]]
            # Risovrascrivo gli angoli di l
            l[0][-1], l[1][0], l[2][0], l[3][-1] = r[-1:] + r[:-1]
            # Reimposto gli angoli nel cubo reale
            self.facce["U"][-1] = l[0][-1]
            self.facce["R"] = trasposizione(l[1])
            self.facce["D"][0] = l[2][0]
            self.facce["L"] = trasposizione(l[3])
        # Se la faccia è quella a sinistra
        elif faccia == "R":
            # Ruoto verticalmente
            self.ruota_verticalmente()
            # Modifico le facce in base a Front
            self.modifica_faccia_adiacente("F")
            # Ruoto verticalmente in senso inverso per ripristinare
            self.ruota_verticalmente(inverso=True)
        # Se la faccia è quella a destra
        elif faccia == "L":
            # Ruoto verticalmente in senso inverso
            self.ruota_verticalmente(inverso=True)
            # Modifico le facce in base a Front
            self.modifica_faccia_adiacente("F")
            # Ruoto nuovamente verticalmente per ripristinare
            self.ruota_verticalmente()
        # Se la faccia è quella posteriore
        elif faccia == "B":
            # Ruoto verticalmente due volte
            self.ruota_verticalmente(due_volte=True)
            # Modifico le facce in base a Front
            self.modifica_faccia_adiacente("F")
            # Ruoto nuovamente verticalmente due volte per ripristinare
            self.ruota_verticalmente(due_volte=True)
            
    # Metodo per ruotare una singola faccia
    def ruota(self, movimenti: Movimenti):
        for _ in range(2 if movimenti.due_volte else 3 if movimenti.inverti else 1):
            # Ruoto faccia
            self.ruota_faccia(movimenti.faccia)
            # Sistemo facce adiacenti
            self.modifica_faccia_adiacente(movimenti.faccia)

    # Metodo per ruotare una faccia verticalmente
    def ruota_verticalmente(self, due_volte=False, inverso=False):
        for i in range(2 if due_volte else 3 if inverso else 1):
            # Rotazione delle facce in due metodi 
            # l = self.facce["F"], self.facce["L"], self.facce["B"], self.facce["R"] Creo una lista
            # self.facce["F"] = l[-1] Switcho
            # self.facce["L"] = l[0] Switcho
            # self.facce["B"] = l[1] Switcho
            # self.facce["R"] = l[2] Switcho
            l = [self.facce[faccia] for faccia in ["F", "L", "B", "R"]]
            self.facce["F"], self.facce["L"], self.facce["B"], self.facce["R"] = l[-1:] + l[:-1]
            # Ruoto la faccia Up una volta
            self.ruota_faccia("U")
            # Ruoto la faccia Down tre volte
            for _ in range(3):
                self.ruota_faccia("D")
    
# Metodo per la trasposizione di righe e colonne
T = TypeVar("T")
def trasposizione(l: List[List[T]]) -> List[List[T]]:
    return [list(i) for i in zip(*l)]
