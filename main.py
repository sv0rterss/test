from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from random import randint
app = QApplication([])

window = QWidget()
window.resize(200,200)
window.move(250,250)

button = QPushButton('натисни')
text1 = QLabel('Випадкове число')
text2 = QLabel("?")


v = QVBoxLayout()
v.addWidget(text1,alignment=Qt.AlignCenter)
v.addWidget(text2,alignment=Qt.AlignCenter)
v.addWidget(button,alignment=Qt.AlignCenter)
window.setLayout(v)

def random_number():
    n = randint(1,101)
    text2.setText(str(n))

button.clicked.connect(random_number)

button.setStyleSheet("""
    background-color: #4CAF50;
    border-radius: 10px;
    font-size: 16px;
    border: none;
    padding: 10px 20px;                                      
""")

window.setStyleSheet("""
    background-color: red;
    border-radius: 10px;
    font-size: 16px;
    border: none;                              
""")

window.show()
app.exec_()