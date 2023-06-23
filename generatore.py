from typing import List

import random

# Genera una serie composta da più serie di movimenti casuali
def gen_n_seq_mov_casuali(n: int) -> List[str]:
    serie_mov_c = []

    for _ in range(n):
        serie_mov_c.append(gen_seq_mov_casuali())

    return serie_mov_c

# Genera una serie di movimenti casuali tra i molteplici movimenti disponibili
def gen_seq_mov_casuali() -> str:
    movimenti = ["U", "R", "L", "B", "D", "F"]

    serie_mov_c = []

    for _ in range(40):
        rand_num = random.randint(0, 3) == 0

        if rand_num == 0:
            serie_mov_c.append(random.choice(movimenti))
        elif rand_num == 1:
            serie_mov_c.append(random.choice(movimenti) + "2")
        else:
            serie_mov_c.append(random.choice(movimenti) + "'")

    return " ".join(serie_mov_c)
