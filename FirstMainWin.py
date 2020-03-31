import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()
        # set title for main window
        self.setWindowTitle("First window")
        # set window size
        self.resize(400, 300)
        self.status = self.statusBar()
        self.status.showMessage("Only show 5 seconds", 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./Images/Dragon.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
