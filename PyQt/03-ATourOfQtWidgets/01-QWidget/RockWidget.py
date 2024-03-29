from PySide6.QtWidgets import QPushButton,QWidget,QHBoxLayout,QVBoxLayout

class RockWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("RockWidget")
		# button init
		button1 = QPushButton("Button1")
		button2 = QPushButton("Button2")
		# end button init

		# layout Horizontal
		# button_layout = QHBoxLayout()
		# button_layout.addWidget(button2)
		# button_layout.addWidget(button1)
		# self.setLayout(button_layout)
		# end layout

		# layout Vertical
		button_layout = QVBoxLayout()
		button_layout.addWidget(button2)
		button_layout.addWidget(button1)
		self.setLayout(button_layout)
		# end layout Vertical

		# button signal connect
		button1.clicked.connect(self.button1_clicked)
		button2.clicked.connect(self.button2_clicked)
		# end button signal connect


	def button1_clicked(self):
		print("Button1 clicked")

	def button2_clicked(self):
		print("Button2 clicked")