from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                              QLineEdit, QVBoxLayout, QListWidget)
                            
app = QApplication([])
window = QWidget()
window.resize(300,450)
window.move(250,250)

button1 = QPushButton("добавити")
button2 = QPushButton("видалити")
button3 = QPushButton("зберегти")

line = QLineEdit()
list1 = QListWidget()

v = QVBoxLayout() 
v.addWidget(line)
v.addWidget(button1)
v.addWidget(list1)
v.addWidget(button2)
v.addWidget(button3)
window.setLayout(v)


tasks = []
def add_task():
    t = line.text()
    if t:
        tasks.append(t)
        list1.addItem(t)
        line.clear()
button1.clicked.connect(add_task)

def remove_task():
    t = list1.currentRow()
    if t >= 0:
        del tasks[t]
        list1.takeItem(t)

button2.clicked.connect(remove_task) 


def save_task():
    with open("tasks.txt","w") as file:
        for t in tasks:
            file.write(t+"\n")
button3.clicked.connect(save_task)


window.show()
app.exec()