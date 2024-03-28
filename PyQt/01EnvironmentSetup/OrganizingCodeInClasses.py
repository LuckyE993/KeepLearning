# Version1 Setting everything up in the global scope
"""
from PySide6.QtWidgets import QWidget,QApplication,QPushButton,QMainWindow

import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My App")

button = QPushButton("My Button")
button.setText("Click Me!")

window.setCentralWidget(button)

window.show()
app.exec()

"""

# Version2 Setting up a separate class
"""

import sys
from PySide6.QtWidgets import QWidget,QApplication,QPushButton,QMainWindow


class ButtonHolder(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My App")
		button = QPushButton("My Button")

		# Set up the button as our central widget
		self.setCentralWidget(button)


app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()

"""

# Version3 Organizing code into classes
import sys
from PySide6.QtWidgets import QApplication
import button_holder

app = QApplication(sys.argv)
window = button_holder.ButtonHolder()
window.show()
app.exec()
