from .cubo_rubik.cubo import Cubo
from .cubo_rubik.interfaccia import Gui

# Esecuzione main con chiamata a interfaccia Gui
if __name__ == "__main__":
    cubo = Cubo(3)
    gui = Gui(cubo)
    gui.esegui()