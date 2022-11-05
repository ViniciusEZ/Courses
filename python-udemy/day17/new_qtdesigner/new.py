import sys
from day17.new_qtdesigner.design import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class NewRezise(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.open_image)
        self.BtnRezise.clicked.connect(self.resizing)
        self.BtnSave.clicked.connect(self.save)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open Image',
            '/home/vinicius/imgs',
            options=QFileDialog.DontUseNativeDialog
        )
        self.Input_OpenFile.setText(image)
        self.original_img = QPixmap(image)
        self.LabelImg.setPixmap(self.original_img)
        self.InputWidth.setText(str(self.original_img.width()))
        self.InputHeight.setText(str(self.original_img.height()))

    def resizing(self):
        width = int(self.InputWidth.text())
        self.new_img = self.original_img.scaledToWidth(width)
        self.LabelImg.setPixmap(self.new_img)
        self.InputWidth.setText(str(self.new_img.width()))
        self.InputHeight.setText(str(self.new_img.height()))

    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Save Image',
            '/home/vinicius/',
            options=QFileDialog.DontUseNativeDialog
        )
        self.new_img.save(image, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    new = NewRezise()
    new.show()
    qt.exec_()
