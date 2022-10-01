"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para
criação de aplicações GUI (Interface Gráfica). Também inclui diversas funcionalidades,
como: acesso a base de dados, threads, comunicação de rede, etc...
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Button text')
        self.btn.setStyleSheet('font-size: 50px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.actionz)

        self.setCentralWidget(self.cw)

    def actionz(self):
        print('Hello World...')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
