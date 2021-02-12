# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.14.2
# Cleaned up by: Melvin Chia AKA The Silly Coder


from PyQt5 import QtCore, QtGui, QtWidgets

class FadePushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QtCore.QVariantAnimation(
            startValue=QtGui.QColor("#0086d9"),
            endValue=QtGui.QColor("#00a8ff"),
            valueChanged=self._on_value_changed,
            duration=100,
        )
        self._update_stylesheet(QtGui.QColor("white"), QtGui.QColor("black"))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QtGui.QColor("black")
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor("white")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):

        self.setStyleSheet(
            """
            QPushButton {
                background: %s;
                border-radius: 10px;
                border: 0px;
                color: white;
            }
            """ % (background.name()))

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)

class Ui_root(QtWidgets.QWidget):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.setFixedSize(550, 490)
        self.root.setStyleSheet(
            """
            QMainWindow {
                background: white;
            }
            """
            )

        self.container = QtWidgets.QWidget(self.root)
        self.root.setCentralWidget(self.container)

        self.title_label = QtWidgets.QLabel(self.container)
        self.ip_input = QtWidgets.QLineEdit(self.container)
        self.submit_button = FadePushButton(self.container)
        self.port_input = QtWidgets.QLineEdit(self.container)
        self.status_container = QtWidgets.QWidget(self.container)
        self.status_container_layout = QtWidgets.QHBoxLayout(self.status_container)
        self.status_container_spacer_left = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.status_container_spacer_middle = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.status_container_spacer_right = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.status_icon = QtWidgets.QLabel(self.status_container)
        self.status_text = QtWidgets.QLabel(self.status_container)
        self.status_highlight = QtWidgets.QLabel(self.status_container)
        self.settings_button = QtWidgets.QPushButton(self.container)

    def setupQSS(self):
        self.ip_input.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;
                border-width: 1px;
                border-style: solid;
                border-color: #999999
            }
            """)
        self.submit_button.setStyleSheet(
            """
            QPushButton {
                background: #00a8ff;
                border-radius: 10px;
                border: 0px;
                color: white;
            }
            """)
        self.port_input.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;
                border-width: 1px;
                border-style: solid;
                border-color: #999999
            }
            """)
        self.settings_button.setStyleSheet(
            """
            QPushButton {
                background: white;
                border: 0px;
            }
            """)

    def setupGeometry(self):
        self.title_label.setGeometry(QtCore.QRect(45, 0, 460, 130))
        self.ip_input.setGeometry(QtCore.QRect(115, 130, 320, 65))
        self.submit_button.setGeometry(QtCore.QRect(115, 280, 321, 65))
        self.port_input.setGeometry(QtCore.QRect(115, 205, 321, 65))
        self.status_icon.setGeometry(QtCore.QRect(104, 350, 47, 31))
        self.status_container.setGeometry(QtCore.QRect(-1, 348, 550, 66))
        self.settings_button.setGeometry(QtCore.QRect(175, 430, 200, 55))

    def setupFont(self):
        _title_font = QtGui.QFont("Gotham", 28)
        _normal_font = QtGui.QFont("Gotham", 20)
        _button_font = QtGui.QFont("Gotham", 18)

        self.title_label.setFont(_title_font)
        self.ip_input.setFont(_normal_font)
        self.submit_button.setFont(_normal_font)
        self.port_input.setFont(_normal_font)
        self.status_text.setFont(_normal_font)
        self.status_highlight.setFont(_normal_font)
        self.settings_button.setFont(_button_font)

    def setupSizeRange(self):
        self.status_icon.setMinimumSize(QtCore.QSize(32, 0))
        self.status_icon.setMaximumSize(QtCore.QSize(32, 32))
        self.status_text.setMinimumSize(QtCore.QSize(0, 0))
        self.status_text.setMaximumSize(QtCore.QSize(300, 50))

    def setupAlignment(self):
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ip_input.setAlignment(QtCore.Qt.AlignCenter)
        self.port_input.setAlignment(QtCore.Qt.AlignCenter)
        self.status_text.setAlignment(QtCore.Qt.AlignCenter)

    def setupStatusContainer(self):
        self.status_container_layout.addItem(self.status_container_spacer_left)
        self.status_container_layout.addWidget(self.status_icon)
        #self.status_container_layout.addItem(self.status_container_spacer_middle)
        self.status_container_layout.addWidget(self.status_text)
        self.status_container_layout.addWidget(self.status_highlight)
        self.status_container_layout.addItem(self.status_container_spacer_right)

    def setupButtonIcon(self):
        self.settings_button.setIcon(QtGui.QIcon.fromTheme(":/icon/icons/settings.png"))
        self.settings_button.setIconSize(QtCore.QSize(32, 32))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setWindowTitle(_translate("self.root", "Port Forward Checker"))
        self.title_label.setText(_translate("self.root", "Port Forward Checker"))
        self.ip_input.setPlaceholderText(_translate("self.root", "IP Address"))
        self.submit_button.setText(_translate("self.root", "Check"))
        self.port_input.setPlaceholderText(_translate("self.root", "Port"))
        self.settings_button.setText(_translate("self.root", " settings"))

    def setupValidator(self):
        _ipRegExp = QtCore.QRegExp(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
        _ipValidator = QtGui.QRegExpValidator(_ipRegExp, self)
        _portValidator = QtGui.QIntValidator(1, 65535)
        self.ip_input.setValidator(_ipValidator)
        self.port_input.setValidator(_portValidator)

    def setupCursor(self):
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def setupUi(self):
        self.setupQSS()
        self.retranslateUi()
        self.setupGeometry()
        self.setupFont()
        self.setupSizeRange()
        self.setupStatusContainer()
        self.setupButtonIcon()
        self.setupAlignment()
        self.setupValidator()
        self.setupCursor()
        self.root.setFocus()
        QtCore.QMetaObject.connectSlotsByName(self.root)

import icons_rc
