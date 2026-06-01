import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class Count(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.label = QLabel(str(self.count), self)
        self.button1 = QPushButton("increase", self)
        self.button2 = QPushButton("reset", self)
        self.button3 = QPushButton("decrease", self)
        self.button1.clicked.connect(self.increase)
        self.button2.clicked.connect(self.reset)
        self.button3.clicked.connect(self.decrease)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Counting Program")

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
        QLabel{
            font-size: 60px;
            font-family: Ink Free;
        }
        QPushButton{
            font-family: Ink Free;
            font-size: 50px;
            border: none;
            border-radius: 10px;
        }
        QPushButton#button1{
            background-color: #00ff00;
        }
        QPushButton#button2{
            background-color: #0532fc;
        }
        QPushButton#button3{
            background-color: #ddd;
        }
        """)

    def increase(self):
        self.count += 1
        self.label.setText(str(self.count))

    def reset(self):
        self.count = 0
        self.label.setText(str(self.count))

    def decrease(self):
        self.count -= 1
        self.label.setText(str(self.count))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Count()
    window.show()
    sys.exit(app.exec_())