from typing import List
from copy import deepcopy

from .cubo import Cubo
from .movimenti import Movimenti
from .colore import WHITE, YELLOW, GREEN, BLUE, ORANGE, RED
from .cubo_storico import CuboStorico
from ..mischia.ripulitore import pulisci_movimenti
from ..mischia.controllore import trasf_in_movimenti, trasf_in_stringa

# Funzione per la generazione della soluzione del cubo
def genera_soluzione(cubo: Cubo) -> List[Movimenti]:
    copia_cubo = CuboStorico(cubo.dimensione, deepcopy(cubo.facce))
    # Eseguo i passi della soluzione
    risolvi_croce(copia_cubo)
    risolvi_angoli(copia_cubo)
    risolvi_bordi_2L(copia_cubo)
    risolvi_EOLL(copia_cubo)
    risolvi_OCLL(copia_cubo)
    risolvi_CPLL(copia_cubo)
    risolvi_EPLL(copia_cubo)
    # Trasformazione in movimenti della lista di stringhe e ritorno della stessa
    return trasf_in_movimenti(pulisci_movimenti(trasf_in_stringa(copia_cubo.get_lista_mov_storici())))

# Funzione per la risoluzione della croce sulla faccia superiore
def risolvi_croce(cubo: CuboStorico):
    # Creo un dizionario riguardante i bordi della faccia 
    BORDI = {
        "UF": "",
        "UL": "U'",
        "UR": "U",
        "UB": "U2",
        "LB": "L U' L'",
        "LD": "L2 U'",
        "LF": "L' U' L",
        "RB": "R' U R",
        "RD": "R2 U",
        "RF": "R U R'",
        "DB": "B2 U2",
        "DF": "F2"
    }
    # Ciclo su ogni colore dei quattro centri laterali
    for colore in [BLUE, ORANGE, GREEN, RED]:
        # Ciclo sui bordi di contorno
        for bordo in BORDI:
            # Salvo il bordo corrente
            bordo_corrente = tuple(cubo.get_bordo(bordo).values())
            # Se il bordo ha il giallo in uno dei due sticker possibili combinati
            if bordo_corrente in [(colore, YELLOW), (YELLOW, colore)]:
                # Eseguo movimenti rispetto al bordo selezionato
                cubo.esegui_movimenti(BORDI[bordo])
                # Controllo se il bordo UpFront nella faccia Up è effettivamente giallo
                if cubo.get_bordo("UF")["U"] == YELLOW:
                    # Eseguo rotazione Front due volte
                    cubo.esegui_movimenti("F2")
                else:
                    # Eseguo altri movimenti
                    cubo.esegui_movimenti("R U' R' F")
                # Movimento finale per seguire l'algoritmo
                cubo.esegui_movimenti("D'")
                break
    # Ruoto Down due volte per l'algoritmo
    cubo.esegui_movimenti("D2")

# Funzione per la risoluzione degli angoli sulla faccia superiore
def risolvi_angoli(cubo: Cubo):
    # Creo un dizionario riguardante gli angoli della faccia e i singoli movimenti per risolverli
    ANGOLI = {
        "UFR": "U2 U2",
        "DFR": "R U R' U'",
        "DBR": "R' U R U",
        "URB": "U",
        "ULF": "U'",
        "UBL": "U2",
        "DFL": "L' U' L",
        "DBL": "L U L' U" 
    }
    # Ciclo su ogni possibile coppia di colori dell'angolo (coppia perchè il giallo lo inserisco dopo)
    for colore1, colore2 in [(GREEN, RED), (BLUE, RED), 
                             (BLUE, ORANGE), (GREEN, ORANGE)]:
        # Ciclo sul dizionario degli angoli
        for angolo in ANGOLI:
            # Rilevo l'angolo che mi serve
            angolo_corr = cubo.get_angolo(angolo).values()
            # Rilevo un angolo che ha tra i colori il giallo
            if colore1 in angolo_corr and colore2 in angolo_corr and YELLOW in angolo_corr:
                # Eseguo movimenti rispetto all'angolo selezionato
                cubo.esegui_movimenti(ANGOLI[angolo])
                # Rilevo lo sticker in esame e lo comparo
                if cubo.get_sticker("UFR") == YELLOW:
                    # Compongo una serie di movimenti
                    movimenti = "U R U2 R' U R U' R'"
                # Rilevo lo sticker in esame e lo comparo
                elif cubo.get_sticker("FUR") == YELLOW:
                    # Compongo una serie di movimenti
                    movimenti = "U R U' R'"
                else:
                    # Compongo una serie di movimenti
                    movimenti = "R U R'"
                # Eseguo movimenti definiti
                cubo.esegui_movimenti(movimenti)
                # Movimento finale per seguire l'algoritmo
                cubo.esegui_movimenti("D'")
                break
    
# Metodo per risolvere i bordi del secondo livello
def risolvi_bordi_2L(cubo: Cubo):
    # Creo un dizionario riguardante i bordi della faccia e i singoli movimenti per risolverli
    BORDI = {
        "UF": "U2 U2",
        "UR": "U",
        "UL": "U'",
        "UB": "U2",
        "RF": "R' F R F' R U R' U'",
        "LF": "L F' L' F L' U' L U",
        "RB": "R' U R B' R B R'",
        "LB": "L U' L' B L' B' L"
    }
    # Ciclo su ogni possibile coppia di colori del bordo
    for colore1, colore2 in [(GREEN, RED), (RED, BLUE), (BLUE, ORANGE), (ORANGE, GREEN)]:
        # Ciclo sul dizionario dei bordi
        for bordo in BORDI:
            # Rilevo il bordo che mi serve
            bordo_corrente = tuple(cubo.get_bordo(bordo).values())
            # Controllo se il bordo è presente in una combinazione definita precedentemente
            if bordo_corrente == (colore1, colore2) or bordo_corrente == (colore2, colore1):
                # Eseguo movimenti rispetto al bordo rilevato
                cubo.esegui_movimenti(BORDI[bordo])
                # Rilevo lo sticker in FrontUp e lo comparo a uno dei quattro colori
                if cubo.get_sticker("FU") == colore1:
                    # Compongo una serie di movimenti
                    movimenti = "U R U' R' F R' F' R"
                else:
                    # Compongo una serie di movimenti
                    movimenti = "U2 R' F R F' R U R'"
                # Eseguo movimenti definiti
                cubo.esegui_movimenti(movimenti)
                # Movimento finale per seguire l'algoritmo per posizionare la faccia successiva
                cubo.esegui_movimenti("y")
                break

# Metodo per orientare i bordi finali (Edge Oriented Last Layer)
def risolvi_EOLL(cubo: Cubo):
    # Ciclo sui possibili quattro bordi
    for _ in range(4):
        # Creo una lista che contiene i colori dei bordi nelle posizioni UpBack UpRight UpFront UpLeft
        terzo_livello = [cubo.get_sticker("UB"), cubo.get_sticker("UR"),
                     cubo.get_sticker("UF"), cubo.get_sticker("UL")]
        # Condizione di orientamento se e solo se è presente il bianco nelle combinazioni
        cond_eo = [faccia == WHITE for faccia in terzo_livello]
        # Se in nessuna faccia c'è il bianco 
        if cond_eo == [False, False, False, False]:
            # Eseguo movimenti necessari
            cubo.esegui_movimenti("R U2 R2 F R F' U2 R' F R F'")
            break
        # Se in UpFront e UpLeft è presente il bianco
        elif cond_eo == [False, False, True, True]:
            # Eseguo movimenti necessari
            cubo.esegui_movimenti("U F U R U' R' F''")
            break
        # Se in UpRight e UpLeft è presente il bianco
        elif cond_eo == [False, True, False, True]:
            # Eseguo movimenti necessari
            cubo.esegui_movimenti("F R U R' U' F'")
            break
        # Eseguo movimenti necessari 
        else:
            cubo.esegui_movimenti("U")

# Metodo per orientare gli angoli finali (Orientation and Corner Last Layer)
def risolvi_OCLL(cubo: Cubo):
    # Creazione di un dizionario utile a definire quali movimenti realizzare in base all'orientamento
    DIZ_OCLL = {
        "S": "R U R' U R U2 R' U", # Angoli finali non sono correttamente orientati e la faccia superiore non ha sticker bianchi
        "AS": "U R' U' R U' R' U2 R", # Angoli finali non sono correttamente orientati e la faccia superiore ha solo un sticker bianco
        "H": "F R U R' U' R U R' U' R U R' U' F'", # Angoli finali non sono correttamente orientati e la faccia superiore ha due sticker bianchi adiacenti
        "Headlights": "R2 D' R U2 R' D R U2 R", # Angoli finali non sono correttamente orientati e la faccia superiore ha due sticker bianchi opposti
        "Sidebars": "U' L F R' F' L' F R F'", # Angoli finali non sono correttamente orientati e la faccia superiore ha tre sticker bianchi
        "Fish": "R' U2 R' D' R U2 R' D R2", # Angoli finali non sono correttamente orientati e la faccia superiore ha un solo sticker bianco
        "Pi": "U R U2 R2 U' R2 U' R2 U2 R" # Angoli finali non sono correttamente orientati e la faccia superiore non ha sticker bianchi
    }
    # Metodo per ritornare il colore degli sticker negli angoli finali
    def get_sticker_finali(cubo: Cubo):
        return [cubo.get_sticker("UBL"), cubo.get_sticker("UBR"),
                cubo.get_sticker("UFR"), cubo.get_sticker("UFL")]
    # Metodo per controllare il corretto orientamento
    def get_or_corretto(terzo_livello):
        # Itero su ogni faccia e controllo se il quadrato in esame è effettivamente bianco
        return [faccia == WHITE for faccia in terzo_livello]
    # Ciclo sui quattro possibili orientamenti
    for _ in range(4): 
        # Creo variabile sullo stato di orientamento
        stato_orient = get_or_corretto(get_sticker_finali(cubo))
        # Controllo i possibili stati di orientamento
        if stato_orient == [False, False, False, False]:
            # Eseguo fino a quando non rilevo o lo sticker bianco su FrontUpRight o FrontUpLeft
            while cubo.get_sticker("FUR") != WHITE or cubo.get_sticker("FUL") != WHITE:
                # Eseguo movimenti necessari
                cubo.esegui_movimenti("U")
            # Controllo se l'angolo hanno UpFrontRight e UpBackLeft hanno lo stesso sticker colorato
            if cubo.get_angolo("UFR")["F"] == cubo.get_angolo("UBL")["B"]: 
                # Eseguo movimenti ottenuti da dizionario 
                cubo.esegui_movimenti(DIZ_OCLL["H"])
            else:
                # Eseguo movimenti ottenuti da dizionario
                cubo.esegui_movimenti(DIZ_OCLL["Pi"])
            break
        # Controllo i possibili stati di orientamento
        elif stato_orient == [False, False, False, True]:
            # Controllo se FrontUpRight ha lo sticker bianco
            if cubo.get_sticker("FUR") == WHITE:
                # Eseguo movimenti ottenuti da dizionario
                cubo.esegui_movimenti(DIZ_OCLL["S"])
            else:
                # Eseguo movimenti ottenuti da dizionario
                cubo.esegui_movimenti(DIZ_OCLL["AS"])
            break
        # Controllo i possibili stati di orientamento
        elif stato_orient == [False, False, True, True]:
            # Controllo se BackRightUp ha lo sticker bianco
            if cubo.get_sticker("BRU") == WHITE:
                # Eseguo movimenti ottenuti da dizionario
                cubo.esegui_movimenti(DIZ_OCLL["Headlights"])
            else:
                # Eseguo movimenti ottenuti da dizionario
                cubo.esegui_movimenti(DIZ_OCLL["Sidebars"])
            break
        # Controllo i possibili stati di orientamento
        elif stato_orient == [False, True, False, True]:
            # Controllo se RightUpFront ha lo sticker non bianco
            if cubo.get_sticker("RUF") != WHITE:
                # Eseguo movimenti necessari
                cubo.esegui_movimenti("U2")
                # Eseguo movimenti ottenuti da dizionario
            cubo.esegui_movimenti(DIZ_OCLL["Fish"])
            break
        else:
            # Eseguo movimenti necessari
            cubo.esegui_movimenti("U")

# Metodo per permutare e orientare gli angoli finali (Corner Permutation and Corner Orientation Last Layer)
def risolvi_CPLL(cubo: Cubo):
    # Definizione dell'algoritmo di soluzione di una possibile situazione
    alg = "R' U L' U2 R U' R' U2 R L "
    # Itero possibilmente fino alle quattro possibili situazioni
    for _ in range(4):
        # Controllo sul colore degli sticker degli angoli in esame
        if cubo.get_sticker("FUR") == cubo.get_sticker("FUL") and cubo.get_sticker("BLU") == cubo.get_sticker("BRU"):
            # Situazione corretta
            break
        # Controllo sul colore degli sticker degli angoli in esame
        if cubo.get_sticker("FRU") == cubo.get_sticker("FLU"):
            # Eseguo movimenti dell'algoritmo necessario a sistemarli
            cubo.esegui_movimenti(alg)
            break
        # Eseguo movimenti necessari in quanto almeno uno degli angoli non risulta corretto
        cubo.esegui_movimenti("U")
    else:
        # Tutti gli angoli tranne uno sono corretti allora..
        # ..Eseguo alg + rotazione di Up + algoritmo nuovamente per risolvere 
        cubo.esegui_movimenti(alg + " U " + alg)

# Metodo per permutare e orientare i bordi finali (Edge Permutation and Edge Orientation Last Layer)
def risolvi_EPLL(cubo: Cubo):
    bordi_risolti = 0
    # Ciclo sulle quattro possibili combinazioni
    for _ in range(4):
        # Controllo se FrontUp ha lo stesso colore anche a destra FrontUpRight il ché vuol dire che è corretto
        if cubo.get_sticker("FU") == cubo.get_sticker("FUR"):
            # Aumento i bordi risolti
            bordi_risolti += 1
        # Ruoto la faccia Up
        cubo.esegui_movimenti("U")
    # Controllo se i bordi non sono risolti 
    if bordi_risolti != 4:
        # Controllo sul numero di bordi risolti
        if bordi_risolti == 0:
            # Eseguo movimenti necessari per questa situazione
            cubo.esegui_movimenti("R U' R U R U R U' R' U' R2")
        # Fino a quando FrontUp e FrontUpRight non hanno il colore corretto
        while cubo.get_sticker("FU") != cubo.get_sticker("FUR"):
            # Ruoto la faccia Up
            cubo.esegui_movimenti("U")
        # Ruoto la faccia Up due volte consecutive
        cubo.esegui_movimenti("U2")
        # Fino a quando FU e FUR non hanno il colore corretto
        while cubo.get_sticker("FU") != cubo.get_sticker("FUR"):
            # Eseguo movimenti necessari per questa situazione
            cubo.esegui_movimenti("R U' R U R U R U' R' U' R2")
    # Fino a quando FrontUp e FrontRight non hanno il colore corretto
    while cubo.get_sticker("FU") != cubo.get_sticker("FR"):
        # Ruoto la faccia Up
        cubo.esegui_movimenti("U") 