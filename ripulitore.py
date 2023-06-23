# Classe utile a ripulire movimenti inutili nel mischiare o nel risolvere il cubo
def pulisci_movimenti(seq_per_mischiare):
    # Separo movimento per movimento la sequenza
    seq_separata_movim = seq_per_mischiare.split()
    seq = 0
    # Ciclo su ogni movimento
    while seq < len(seq_separata_movim):
        try:
            # Controllo sui primi due movimenti consecutivi
            if seq_separata_movim[seq][0] == seq_separata_movim[seq + 1][0]:
                # Se il primo movimento non è invertito né ripetuto
                if not e_invertito(seq_separata_movim[seq]) and not e_ripetuto(seq_separata_movim[seq]):
                    # Se il secondo movimento non è invertito né ripetuto
                    if not e_invertito(seq_separata_movim[seq + 1]) and not e_ripetuto(seq_separata_movim[seq + 1]):
                        # Elimino il secondo movimento e ripeto il primo due volte consecutive
                        del seq_separata_movim[seq + 1]
                        seq_separata_movim[seq] += "2"

                    # Secondo movimento è invertito
                    elif e_invertito(seq_separata_movim[seq + 1]):
                        # Elimino il primo e il secondo movimento in quanto si equibilanciano
                        del seq_separata_movim[seq], seq_separata_movim[seq]

                    # Secondo movimento ripetuto
                    elif e_ripetuto(seq_separata_movim[seq + 1]):
                        # Elimino il secondo movimento e modifico il precedente
                        del seq_separata_movim[seq + 1]
                        seq_separata_movim[seq] += "'"

                # Se il primo movimento è invertito
                elif e_invertito(seq_separata_movim[seq]):
                    # Secondo movimento non è invertito né ripetuto
                    if not e_invertito(seq_separata_movim[seq + 1]) and not e_ripetuto(seq_separata_movim[seq + 1]):
                        # Elimino entrambi i movimenti
                        del seq_separata_movim[seq], seq_separata_movim[seq]

                    # Secondo movimento è invertito
                    elif e_invertito(seq_separata_movim[seq + 1]):
                        # Elimino il secondo e ripeto il primo 
                        del seq_separata_movim[seq + 1]
                        seq_separata_movim[seq] = seq_separata_movim[seq][0] + "2"

                    # Secondo movimento è ripetuto
                    elif e_ripetuto(seq_separata_movim[seq + 1]):
                        # Elimino il secondo movimento e non modifico il primo
                        del seq_separata_movim[seq + 1]
                        seq_separata_movim[seq] = seq_separata_movim[seq][0]


                # Se il primo movimento è ripetuto
                elif e_ripetuto(seq_separata_movim[seq]):
                    # Secondo movimento non è invertito né ripetuto
                    if not e_invertito(seq_separata_movim[seq + 1]) and not e_ripetuto(seq_separata_movim[seq + 1]):
                        # Elimino il primo movimento e lo sostituisco modificandolo
                        del seq_separata_movim[seq]
                        seq_separata_movim[seq] = seq_separata_movim[seq][0] + "'"

                    # Secondo movimento è invertito
                    elif e_invertito(seq_separata_movim[seq + 1]):
                        # Elimino il secondo movimento e mantengo invariato il primo
                        del seq_separata_movim[seq + 1]
                        seq_separata_movim[seq] = seq_separata_movim[seq][0]

                    # Secondo movimento è ripetuto
                    elif e_ripetuto(seq_separata_movim[seq + 1]):
                        # Elimino entrambi i movimenti
                        del seq_separata_movim[seq], seq_separata_movim[seq]
                
                # Riduco la sequenza di uno se devo ripulire un movimento 
                seq -= 1
        except IndexError:
            break
        seq += 1

    return " ".join(seq_separata_movim)

# Funzione che verifica se il movimento è una ripetizione
def e_ripetuto(movimento):
    try:
        if movimento[1] == "2":
            return True
        else:
            return False
    except IndexError:
        return False

# Funzione che verifica se il movimento è un'inversione
def e_invertito(movimento):
    try:
        if movimento[1] == "'":
            return True
        else:
            return False
    except IndexError:
        return False

# Test di controllo
if __name__ == "__main__":
    ''' 
    print(pulisci_movimenti("U U D D' U U2"))
    print(pulisci_movimenti("U' U D' D' U' U2"))
    print(pulisci_movimenti("U2 U D2 D' U2 U2"))

    print("Correct output is")
    print("U2 U'")
    print("D2 U")
    print("U' D")
    '''
    print(pulisci_movimenti("B R2 B F2 L2 D D2 F2 D2 L B D U2 D2 D2 R R2 L F2 U2"))