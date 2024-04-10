from PySide6.QtWidgets import QPushButton,QMessageBox,QMainWindow,QVBoxLayout,QWidget
class widget(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QMessageBox Demo")
		button_hard = QPushButton("Hard")
		button_hard.clicked.connect(self.button_clicked_hard)

		button_critical = QPushButton("Critical")
		button_critical.clicked.connect(self.button_clicked_critical)

		button_question = QPushButton("Question")
		button_question.clicked.connect(self.button_clicked_question)

		button_information = QPushButton("Information")
		button_information.clicked.connect(self.button_clicked_information)

		button_warning = QPushButton("Warning")
		button_warning.clicked.connect(self.button_clicked_warning)

		button_about = QPushButton("About")
		button_about.clicked.connect(self.button_clicked_about)

		# Set up the layouts
		layout = QVBoxLayout()
		layout.addWidget(button_hard)
		layout.addWidget(button_critical)
		layout.addWidget(button_question)
		layout.addWidget(button_information)
		layout.addWidget(button_warning)
		layout.addWidget(button_about)
		self.setLayout(layout)

	# The hard way : critical
	def button_clicked_hard(self):
		print("User chose Hard")

	# Critical
	def button_clicked_critical(self):
		print("User chose Critical")

	# Question
	def button_clicked_question(self):
		print("User chose Question")

	# Information
	def button_clicked_information(self):
		print("User chose Information")

	# Warning
	def button_clicked_warning(self):
		print("User chose Warning")

	# About
	def button_clicked_about(self):
		print("User chose About")