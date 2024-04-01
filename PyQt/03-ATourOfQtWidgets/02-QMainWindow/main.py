from PySide6.QtWidgets import QApplication,QMainWindow
import sys
from mainwindow import MainWindow
app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()