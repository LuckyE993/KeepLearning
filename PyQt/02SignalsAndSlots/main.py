# Version1 Just responding to a button click.
"""
from PySide6.QtWidgets import QApplication,  QPushButton
import sys

def button_clicked(data):
	print("Button clicked!",data)

app = QApplication(sys.argv)
button = QPushButton("Click Me!")
button.setCheckable(True)

button.clicked.connect(button_clicked)

button.show()
app.exec()
"""
# Version2 Capture a value from a Slider
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider
import sys

def respond_to_slider(data):
	print("Slider value:",data)

app = QApplication(sys.argv)
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
