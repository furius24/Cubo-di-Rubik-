from typing import List, Dict, Union

from .cubo import Cubo
from .pezzi import Angolo, Bordo, BORDO_A_UF, ANGOLO_A_UFR
from .movimenti import Movimenti
from .colore import Colore
from ..mischia import controllore

# Creazione classe cubostorico per tenere traccia dei movimenti 
class CuboStorico(Cubo):
    # Creazione di un cubo storico
    def __init__(self, dimensione: int, facce: Dict[str, List[List[Colore]]]=None):
        super().__init__(dimensione)
        self.facce = facce if facce else self.facce
        self.storico = []

    # Funzione per ricevere la lista dei movimenti storici
    def get_lista_mov_storici(self) -> List[Movimenti]:
        return self.storico

    # Rileva bordo dal quadrato in esame
    def get_bordo(self, pezzo: str) -> Bordo:
        # Trasformo il bordo in un possibile movimento nel dizionario
        movimenti = controllore.trasf_in_movimenti(BORDO_A_UF[pezzo])
        # Eseguo i movimenti per definirlo
        self.esegui_movimenti(movimenti, False)
        # Compongo le informazioni sui colori del bordo
        info = Bordo({
            pezzo[0]: Colore(self.facce["U"][-1][1]),
            pezzo[1]: Colore(self.facce["F"][0][1])
        })
        # Inverto i movimenti
        self.esegui_movimenti(controllore.inverti_movimenti(movimenti), False)
        # Ritorno le informazioni sul bordo
        return info

    # Rileva angolo dall'angolo in esame
    def get_angolo(self, pezzo: str) -> Angolo:
        # Trasformo l'angolo in un possibile movimento nel dizionario
        movimenti = controllore.trasf_in_movimenti(ANGOLO_A_UFR[pezzo])
        # Eseguo i movimenti riguardanti l'angolo
        self.esegui_movimenti(movimenti, False)
        # Compongo le informazioni sui colori dell'angolo
        info = Angolo({
            # Controlli sulla posizione dell'angolo selezionato
            pezzo[0]: Colore(self.facce["U"][-1][-1]), 
            pezzo[1]: Colore(self.facce["F"][0][-1]),
            pezzo[2]: Colore(self.facce["R"][0][0])
        })
        # Inverto i movimenti eseguiti precedentemente
        self.esegui_movimenti(controllore.inverti_movimenti(movimenti), False)
        # Ritorno le info sull'angolo
        return info

    # Metodo per far salvare i movimenti nello storico del cubo
    def esegui_movimenti(self, movimenti: Union[str, List[Movimenti]], salva_storico: bool=True): 
        super().esegui_movimenti(movimenti)
        # Controllo sulla lista di movimenti
        if isinstance(movimenti, str):
            movimenti = controllore.trasf_in_movimenti(movimenti)
        # Salvo lo storico dei movimenti
        if salva_storico:
            for movimento in movimenti:
                self.storico.append(movimento)
