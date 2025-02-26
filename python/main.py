import sys
import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

sys.path.insert(0, '..')

from ui.main_ui import Ui_MainWindow


class CoffeeApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.con = sqlite3.connect('../data/coffee.sqlite')
        self.update_table()

    def update_table(self):
        result = self.con.cursor().execute('SELECT * FROM coffee').fetchall()

        self.coffee_table.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, val in enumerate(row):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeApp()
    ex.show()
    sys.exit(app.exec())
