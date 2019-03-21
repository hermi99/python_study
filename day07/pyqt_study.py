import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    label = QLabel("hello world")
    button = QPushButton('PyQt5 button')

    layout.addWidget(label)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
