import json

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from main import start_game

app = QApplication([])
settings = {}
def read_data():
    global settings
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)
def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file)
window = QWidget()

read_data()
print(settings)

start_btn = QPushButton("Старт")
change_btn = QPushButton("Change")
skin1 = QLabel("Картинка")
skin1_img = QPixmap("bullet.png")
skin1_img = skin1_img.scaledToWidth(64)
skin1.setPixmap(skin1_img)
skin1_buy_button = QPushButton("Купити скін")
line_edit = QLineEdit(settings["skin"])

main_line = QVBoxLayout()
main_line.addWidget(line_edit)
main_line.addWidget(start_btn)
main_line.addWidget(change_btn)
main_line.addWidget(skin1)
main_line.addWidget(skin1_buy_button)


window.setLayout(main_line)

def skin1_buy():
    if settings["money balance"] >= 20:
        settings["money balance"] -= 20
        settings["skin"] = "bullet.png"
        write_data()
    else:
        print("На превеликий жаль, у вас недостаньо грошей")

skin1_buy_button.clicked.connect(skin1_buy)

def change_data():
    settings["skin"] = line_edit.text()
    write_data()

change_btn.clicked.connect(change_data)

start_btn.clicked.connect(start_game)

window.show()
app.exec()