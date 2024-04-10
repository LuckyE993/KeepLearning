from PySide6.QtWidgets import QApplication
from widget import widget
import sys
app = QApplication(sys.argv)

QMessageBoxDemo = widget()

QMessageBoxDemo.show()

app.exec()

