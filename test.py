import PyQt4.QtGui as qg
import sys


class Widget2(qg.QWidget):
	def __init__(self, parent=None):

		super(Widget2, self).__init__()
		self._set_layout()

	def _set_layout(self):
		pass

class Widget(qg.QWidget):
	def __init__(self, parent=None):
		super(Widget, self).__init__()
		Widget2.__init__(self)
		
		btn = qg.QPushButton(self)
		btn.clicked.connect(self._show)

	def _show(self):
		self.widget2 = Widget2()
		self.widget2.show()


class Window(qg.QMainWindow):
	def __init__(self, parent=None):
		super(Window, self).__init__()
		self._set_layout()

	def _set_layout(self):
		self.widget = Widget()
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
