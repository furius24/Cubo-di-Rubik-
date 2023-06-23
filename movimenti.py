from dataclasses import dataclass

# Creazione di una classe utile alla memorizzazione di dati
@dataclass
class Movimenti:
    # Attributo di tipo stringa che rappresenta la faccia coinvolta nel movimento
    faccia: str
    # Attributo di tipo booleano che indica se il movimento deve essere invertito
    inverti: bool
    # Attributo di tipo booleano che indica se il movimento deve essere eseguito due volte consecutivamente
    due_volte: bool