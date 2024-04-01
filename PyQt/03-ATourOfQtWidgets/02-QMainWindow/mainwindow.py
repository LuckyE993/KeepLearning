# mainwindow.py
from PySide6.QtWidgets import QMainWindow,QToolBar,QPushButton,QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction,QIcon


class MainWindow(QMainWindow):
	def __init__(self, app):
		super().__init__()
		self.app = app
		self.setWindowTitle("My App")

		menubar = self.menuBar()  # add menubar

		file_menu = menubar.addMenu("&File")  # add file menu
		quit_action = file_menu.addAction("Quit")  # add Quit-menu
		quit_action.triggered.connect(self.quit_app)  # add function to quit the window

		edit_menu = menubar.addMenu("Edit")
		edit_menu.addAction("Copy")  # recursive
		edit_menu.addAction("Paste")
		edit_menu.addAction("Cut")
		edit_menu.addAction("Undo")
		edit_menu.addAction("Redo")

		windows_menu = menubar.addMenu("Windows")
		windows_menu.addAction("New Window")

		setting_menu = menubar.addMenu("Setting")
		help_menu = menubar.addMenu("Help")

		tool_bar = QToolBar("My Main Tool Bar")

		tool_bar.setIconSize(QSize(16, 16))
		self.addToolBar(tool_bar)
		tool_bar.addAction(quit_action)

		action1 = QAction("Action1", self)
		action1.setStatusTip("This is action1")
		action1.triggered.connect(self.tool_bar_click)
		tool_bar.addAction(action1)

		action2 = QAction(QIcon("setup.png"), "Action2", self)
		action2.setStatusTip("This is action2")
		action2.triggered.connect(self.tool_bar_click)
		action2.setCheckable(False)
		tool_bar.addAction(action2)

		tool_bar.addSeparator()
		tool_bar.addWidget(QPushButton("Click here"))

		# Working with status bar
		self.setStatusBar(QStatusBar(self))

		# add some button
		button = QPushButton("Button", self)
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)

	def button_clicked(self):
		print("button clicked")

	def quit_app(self):
		self.app.quit()


	def tool_bar_click(self):
		print("tool bar click")
		self.statusBar().showMessage("tool bar click", 2000)


