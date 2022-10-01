from validacpf import valida_cpf
from gerador_cpf import gera_cpf
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from design1 import Ui_MainWindow

class GeraValidaCPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGerar.clicked.connect(self.gerar_cpf)
        self.btnValidar.clicked.connect(self.validar_cpf)

    def gerar_cpf(self):
        self.lblReturn.setText(str(gera_cpf()))

    def validar_cpf(self):
        cpf = self.InputValidaCPF.text()
        self.lblReturn.setText(str(valida_cpf(cpf)))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida = GeraValidaCPF()
    gera_valida.show()
    qt.exec_()
