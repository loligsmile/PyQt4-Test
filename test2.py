import test as tk
import PyQt4.QtGui as qg
import sys

app = qg.QApplication(sys.argv)

q = tk.Window()
q.show()
sys.exit(app.exec_())
