import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

sys.path.insert(0, '..')

from ui.editor_ui import Ui_MainWindow


class CoffeeEditorApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.findButton.clicked.connect(lambda: self.find_coffee(True))
        self.editButton.clicked.connect(self.edit)

        self.con = sqlite3.connect('../data/coffee.sqlite')

    def find_coffee(self, update_lineEdits):
        if self.idLineEdit.text() != '':
            result = self.con.cursor().execute('SELECT * FROM coffee WHERE id=?',
                                               (self.idLineEdit.text(), )).fetchone()
            
            if not result:
                return False
            
            if update_lineEdits:
                self.nameLineEdit.setText(result[1])
                self.degreeLineEdit.setText(result[2])
                self.stateLineEdit.setText(result[3])
                self.descriptionLineEdit.setText(result[4])
                self.costLineEdit.setText(str(result[5]))
                self.volumeLineEdit.setText(str(result[6]))

            return True

    def edit(self):
        if self.idLineEdit.text() == '':
            self.con.cursor().execute('INSERT INTO coffee(name, degree, state, description, cost, volume) VALUES(?, ?, ?, ?, ?, ?)',
                                     (self.nameLineEdit.text(),
                                      self.degreeLineEdit.text(),
                                      self.stateLineEdit.text(),
                                      self.descriptionLineEdit.text(),
                                      float(self.costLineEdit.text()),
                                      float(self.volumeLineEdit.text())))

        elif self.find_coffee(False):
            self.con.cursor().execute('UPDATE coffee SET '
                                      'name = ?, '
                                      'degree = ?, '
                                      'state = ?, '
                                      'description = ?, '
                                      'cost = ?, '
                                      'volume = ? '
                                      'WHERE id = ?',
                                      
                                      (self.nameLineEdit.text(),
                                       self.degreeLineEdit.text(),
                                       self.stateLineEdit.text(),
                                       self.descriptionLineEdit.text(),
                                       float(self.costLineEdit.text()),
                                       float(self.volumeLineEdit.text()),
                                       self.idLineEdit.text()))

        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeEditorApp()
    ex.show()
    sys.exit(app.exec())
