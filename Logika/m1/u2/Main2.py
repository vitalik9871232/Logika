from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

main_win = QWidget()

main_win.setWindowTitle('Визначення переможця')
main_win.move(500, 100)
main_win.resize(400, 200)

button = QPushButton('Згенерувати')
text = QLabel('Натисніть, щоб дізнатися переможця')
win = QLabel('?')
line = QVBoxLayout()

line.addWidget(text,alignment=Qt.AlignCenter)
line.addWidget(win,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)

main_win.setLayout(line)

def show_winner():
    number = randint(0,50)
    win.setText(str(number))
    text.setText('Переможець')

button.clicked.connect(show_winner)

main_win.show()
app.exec_()