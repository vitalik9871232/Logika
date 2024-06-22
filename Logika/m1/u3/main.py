from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QRadioButton

def win():
    victory_win = QMessageBox()
    victory_win.setText("Правильно!\nВи виграли гіроскутер")
    victory_win.exec_()

def lose():
    lose = QMessageBox()
    lose.setText("Ні, в 2005 році\nВи виграли фірмовий плакат")
    lose.exec_()

app = QApplication([])

main_wind = QWidget()
main_wind.setWindowTitle('Конкурс від Crazy People')
main_wind.resize(400,200)

question = QLabel("В якому році канал отримав золоту кнопку від YouTube?")

btn1 = QRadioButton("2005")
btn2 = QRadioButton("2010")
btn3 = QRadioButton("2015")
btn4 = QRadioButton("2020")

main_layout = QVBoxLayout()
h_layout1 = QHBoxLayout()
h_layout2 = QHBoxLayout()
h_layout3 = QHBoxLayout()

h_layout1.addWidget(question, alignment = Qt.AlignCenter)
h_layout2.addWidget(btn1, alignment = Qt.AlignCenter)
h_layout2.addWidget(btn2, alignment = Qt.AlignCenter)
h_layout3.addWidget(btn3, alignment = Qt.AlignCenter)
h_layout3.addWidget(btn4, alignment = Qt.AlignCenter)

main_layout.addLayout(h_layout1)
main_layout.addLayout(h_layout2)
main_layout.addLayout(h_layout3)

btn1.clicked.connect(win)
btn2.clicked.connect(lose)
btn3.clicked.connect(lose)
btn4.clicked.connect(lose)

main_wind.setLayout(main_layout)
main_wind.show()
app.exec_()