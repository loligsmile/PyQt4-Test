import test as tk
import test3 as t3
import PyQt4.QtGui as qg
import sys

def lol(a):
	print(a)

app = qg.QApplication(sys.argv)

q = tk.Window()
q.show()

q.widget.widget2.btn.clicked.connect(
	lambda: t3.printer(str(q.widget.widget2.le.text()))
	)

sys.exit(app.exec_())
