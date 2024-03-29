# Separate logic

from PySide6.QtWidgets import QApplication,QWidget
import sys
from RockWidget import RockWidget
app = QApplication(sys.argv)

window = RockWidget()
window.show()

app.exec()
