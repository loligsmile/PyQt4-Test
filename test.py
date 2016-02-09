import PyQt4.QtGui as qg
import sys


class Widget2(qg.QWidget):
	def __init__(self, parent=None):
		super(Widget2, self).__init__()
		self._set_layout()

	def _set_layout(self):
		self.le = qg.QLineEdit(self)
		self.le.show()
		
	def _show(self):
		self.show()
		self.activateWindow()


class Widget(qg.QWidget):
	def __init__(self, parent=None):
		super(Widget, self).__init__()
		self.widget2 = Widget2()

		btn = qg.QPushButton(self)
		btn.clicked.connect(self._show)

	def _show(self):
		self.widget2._show()


class Window(qg.QMainWindow):
	def __init__(self, parent=None):
		super(Window, self).__init__()
		self.widget = Widget()
		self._set_layout()

	def _set_layout(self):
		self.setCentralWidget(self.widget)
		self.resize(700, 400)

	def closeEvent(self, event):
		event.ignore()
		app.quit()


if __name__ == '__main__':
	app = qg.QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
