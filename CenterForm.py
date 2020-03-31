import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()
        # set title for main window
        self.setWindowTitle("First window")
        # set window size
        self.resize(400, 300)
        self.center()

    def center(self):
        # get screen info
        screen = QDesktopWidget().screenGeometry()
        # get window geometry
        size = self.geometry()

        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2

        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./Images/Dragon.ico'))
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())
