from typing import List, Tuple
from ..cubo_rubik.movimenti import Movimenti

# Funzione utile a trasformare una stringa in una lista di movimenti
def trasf_in_movimenti(mischia: str) -> List[Movimenti]:
    movimenti = []

    for movimento in mischia.split():
        e_invertito = "'" in movimento
        e_doppio = "2" in movimento
        movimenti.append(Movimenti(movimento[0], e_invertito, e_doppio))
    return movimenti

# Funzione utile a trasformare una sequenza di movimenti in una stringa che definisce i movimenti
def trasf_in_stringa(movimenti: List[Movimenti]) -> str:
    mischia = []

    for movimento in movimenti:
        mov_corrente = movimento.faccia
        if movimento.due_volte:
            mov_corrente += "2"
        elif movimento.inverti:
            mov_corrente += "'"

        mischia.append(mov_corrente)
    return " ".join(mischia)

# Funzione utilizzata per invertire i movimenti rilevati da una lista di movimenti
def inverti_movimenti(movimenti: List[Movimenti]):
    movimenti_invertiti = []

    for movimento in reversed(movimenti):
        movimento_invertito = Movimenti(movimento.faccia, not movimento.inverti, movimento.due_volte)
        movimenti_invertiti.append(movimento_invertito)
    return movimenti_invertiti

# Test di controllo
if __name__ == "__main__":
    mischia = "L U2 D B' R2 U2 F R B2 U2 R2 U R2 U2 F2 D R2 D F2"
    print(trasf_in_movimenti(mischia))