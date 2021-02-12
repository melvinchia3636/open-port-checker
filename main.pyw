from PyQt5 import QtCore, QtGui, QtWidgets
from title import Ui_root
import threading
import requests
import socket
import sys

class Thread:
	def __init__(self, ui):
		self.ui = ui

	def run(self):
		self.ui.status_icon.hide()
		self.ui.status_highlight.hide()
		self.ui.status_text.setText('optaining port status')
		self.a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if int(self.ui.port_input.text()) <= 65535:
			_status = self.a_socket.connect_ex((self.ui.ip_input.text(), int(self.ui.port_input.text())))
			if not _status:
				self.ui.status_text.setText('port {} is'.format(self.ui.port_input.text()))
				self.ui.status_icon.setStyleSheet("QLabel {image: url(:/icon/icons/port open.png)}")
				self.ui.status_highlight.setStyleSheet('QLabel {color:#4cd137}')
				self.ui.status_highlight.setText('OPEN')
				self.ui.status_icon.show()
				self.ui.status_highlight.show()
			else:
				self.ui.status_text.setText('port {} is'.format(self.ui.port_input.text()))
				self.ui.status_icon.setStyleSheet("QLabel {image: url(:/icon/icons/port close.png)}")
				self.ui.status_highlight.setStyleSheet('QLabel {color:#e84118}')
				self.ui.status_highlight.setText('CLOSE')
				self.ui.status_icon.show()
				self.ui.status_highlight.show()
		else:
			self.ui.status_text.setText('invalid port')

class Main(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super().__init__()
		self.ui = Ui_root(self)
		self.ui.setupUi()
		self.ui.ip_input.setText(requests.get('http://ip.42.pl/raw').content.decode('utf-8'))
		self.ui.submit_button.clicked.connect(self.check_port)
		self.show()

	def check_port(self):
		thread = Thread(self.ui)
		threading.Thread(target=thread.run).start()

app = QtWidgets.QApplication(sys.argv)
window = Main()
app.exec_()