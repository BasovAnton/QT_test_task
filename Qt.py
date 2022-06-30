import PySide2
from PySide2 import QtWidgets, QtCore, QtGui

from main import Game
from area2 import Ui_Form
#from help import Ui_Help
x = Game()


class MirrorWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #self.ui.pushButton_help.clicked.connect(self.help)
        self.ui.pushButton_start.clicked.connect(self.start_new_game)
        self.ui.pushButton_up.clicked.connect(self.turn_player)
        self.ui.pushButton_down.clicked.connect(self.turn_player)
        self.ui.pushButton_left.clicked.connect(self.turn_player)
        self.ui.pushButton_right.clicked.connect(self.turn_player)

    @QtCore.Slot()
    def display_output(self):
        color_le = {0: 'background-color: red',
                    2: 'background-color: LemonChiffon',
                    4: 'background-color: PapayaWhip',
                    8: 'background-color: PeachPuff',
                    16: 'background-color: LightSalmon',
                    32: 'background-color: Salmon',
                    64: 'background-color: DarkSalmon',
                    128: 'background-color: Coral',
                    256: 'background-color: Tomato',
                    512: 'background-color: Crimson',
                    1024: 'background-color: FireBrick',
                    2048: 'background-color: DarkRed'}

        for index, horizontal_layout in enumerate(self.ui.verticalLayout.children()):
            for index_ in range(horizontal_layout.count()):
                value_for_set = x.field[index][index_]
                item = horizontal_layout.itemAt(index_).widget()
                item.setText(str(value_for_set))
                item.setStyleSheet(color_le.get(value_for_set))

    @QtCore.Slot()
    def start_new_game(self):
        x.clear_fild()
        x.add_two()
        self.ui.lcdNumber.display(x.show_score())
        self.display_output()

    @QtCore.Slot()
    def turn_player(self):
        tern = {"Вверх": "w",
                "Вниз": "s",
                "Влево": "a",
                "Вправо": "d"}
        x.input_play(tern.get(self.sender().text()))
        self.display_output()
        x.add_two()
        self.display_output()
        self.ui.lcdNumber.display(x.show_score())

    # @QtCore.Slot()
    # def help(self):
    #     self.help = HelpApp()
    #     self.help.show()

    # @QtCore.Slot()
    # def closeEvent(self, event: QtGui.QCloseEvent) -> None:
    #     self.help.close()
    #     event.accept()


# class HelpApp(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_Help()
#         self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MirrorWindow()
    win.show()

    app.exec_()
