import PySide2
from PySide2 import QtWidgets, QtCore, QtGui

from main import Game
from area import Ui_Form

x = Game()


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_start.clicked.connect(self.start_new_game)
        self.ui.pushButton_up.clicked.connect(self.turn_player)
        self.ui.pushButton_down.clicked.connect(self.turn_player)
        self.ui.pushButton_left.clicked.connect(self.turn_player)
        self.ui.pushButton_right.clicked.connect(self.turn_player)


    def keyPressEvent(self, event:PySide2.QtGui.QKeyEvent) -> None:

        if event.text().lower() in ['w', 'ц']:
            self.turn_player(event.text().lower())

    @QtCore.Slot()
    def display_output(self):
        color_le = {0: 'background-color: red',
                    2: 'background-color: blue',
                    4: 'background-color: yellow',
                    8: 'background-color: green',
                    16: 'background-color: grey',
                    }

        for index, horizontal_layout in enumerate(self.ui.verticalLayout.children()):
            for index_ in range(horizontal_layout.count()):
                value_for_set = x.field[index][index_]
                item = horizontal_layout.itemAt(index_).widget()
                item.setText(str(value_for_set))
                item.setStyleSheet(color_le.get(value_for_set))

    @QtCore.Slot()
    def start_new_game(self):
        x.clear_field()
        x.add_two()
        self.ui.lcdNumber.display(x.show_score())
        self.display_output()

    @QtCore.Slot()
    def turn_player(self, key=None):
        tern = {"Вверх": "w",
                "Вниз": "s",
                "Влево": "a",
                "Вправо": "d"}
        if key is None:
            x.input_play(tern.get(self.sender().text()))
        else:
            x.input_play(key)
        self.display_output()
        x.add_two()
        self.display_output()
        self.ui.lcdNumber.display(x.show_score())


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()
    app.exec_()
