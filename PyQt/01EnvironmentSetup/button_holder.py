from PySide6.QtWidgets import QPushButton,QMainWindow


class ButtonHolder(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My App")
		button = QPushButton("My Button")

		# Set up the button as our central widget
		self.setCentralWidget(button)
