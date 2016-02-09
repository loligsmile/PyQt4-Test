from PyQt4 import QtGui, QtCore 
import sys


class Widget2(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Widget2, self).__init__()
		self.foo = 'jolo'
		self._set_layout()

	def _set_layout(self):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)

		self.le = QtGui.QLineEdit(self)
		self.btn = QtGui.QPushButton('Print Entry to Terminal', self)
		
		grid.addWidget(self.le, 0, 0)
		grid.addWidget(self.btn, 1, 0)
		
	def _show(self):
		self.show()
		self.activateWindow()


class Widget(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Widget, self).__init__()
		self.widget2 = Widget2()

		btn = QtGui.QPushButton('Open Widget2', self)
		btn.clicked.connect(self._show)

	def _show(self):
		self.widget2._show()


class Window(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(Window, self).__init__()
		self.widget = Widget()
		self._set_layout()

	def _set_layout(self):
		self.setCentralWidget(self.widget)
		self.resize(700, 400)

	def closeEvent(self, event):
		event.ignore()
		QtCore.QCoreApplication.instance().quit()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
