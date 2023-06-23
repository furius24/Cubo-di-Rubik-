
import time
import pygame
from pygame.locals import *

from .cubo import Cubo
from .movimenti import Movimenti
from ..mischia.controllore import trasf_in_movimenti, trasf_in_stringa
from ..mischia.generatore import gen_seq_mov_casuali
from ..mischia.ripulitore import pulisci_movimenti
from .risolutore import genera_soluzione

# Definizione istanze riguardanti le varie dimensioni dell'interfaccia
ALTEZZA = 780
LARGHEZZA = 1240
DIM_QUADRATI = 70
START_ORIZZONTALE = 60

# Definizione classe per l'interfaccia grafica di gioco
class Gui:
    # Creazione istanze della classe per il loro utilizzo e controllo
    def __init__(self, cubo: Cubo):
        self.cubo = cubo
        self.screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
    
    # Definizione delle possibili azioni realizzabili all'interno dell'interfaccia grafica
    def esegui(self):
        self.disegna_cubo()
        esecuz = True
        while esecuz:
            # Controllo di un possibile evento da tastiera
            for event in pygame.event.get():
                maiuscolo = pygame.key.get_pressed()[pygame.K_LSHIFT]
                # Se si vuole uscire
                if event.type == pygame.QUIT:
                    esecuz = False
                
                # Evento tasto da tastiera da rilevare
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)

                    # Controllo sul tipo di tasto
                    if key in {"u", "f", "l", "r", "d", "b"}:
                        self.cubo.ruota(Movimenti(key.upper(), maiuscolo, False))
                        self.disegna_cubo()
                    elif key == "s":
                        self.cubo = Cubo(3)
                        self.cubo.esegui_movimenti(gen_seq_mov_casuali())
                        self.disegna_cubo()
                    elif event.key == pygame.K_SPACE:
                        # Ricevo soluzione dal metodo e la eseguo
                        soluzione = trasf_in_stringa(genera_soluzione(self.cubo))
                        for movimento in soluzione.split():
                            self.cubo.esegui_movimenti(movimento)
                            self.disegna_cubo()
                            time.sleep(0.1)
    
    # Funzione per la rappresentazione del cubo all'interno dell'interfaccia 
    def disegna_cubo(self):
        # Triplo loop per iterare ogni matrice passando da faccia, riga e quadrato corrispondente
        for faccia, facce in enumerate(["U", "F", "D", "B", "L", "R"]):
            for riga, righe in enumerate(self.cubo.facce[facce]):
                for quadrato, quadrati in enumerate(righe):
                    if facce == "L":
                        faccia = 1
                        aggiustamento_orizzontale = - self.cubo.dimensione * DIM_QUADRATI
                    elif facce == "R":
                        faccia = 1
                        aggiustamento_orizzontale = self.cubo.dimensione * DIM_QUADRATI
                    elif facce == "B":
                        faccia = 1
                        aggiustamento_orizzontale = 2 * self.cubo.dimensione * DIM_QUADRATI
                    else:
                        aggiustamento_orizzontale = 0

                    # Aggiustamento coordinate per il posizionamento
                    x = LARGHEZZA / 3 + quadrato * DIM_QUADRATI + aggiustamento_orizzontale
                    y = self.cubo.dimensione * faccia * DIM_QUADRATI + riga * DIM_QUADRATI + START_ORIZZONTALE
                    
                    # Disegno del quadrato e bordo 
                    pygame.draw.rect(self.screen, quadrati, (x, y, DIM_QUADRATI, DIM_QUADRATI), 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), (x, y, DIM_QUADRATI, DIM_QUADRATI), 5)

        # Aggiornamento display
        pygame.display.update()
