import sys, socket
from PyQt5 import QtCore, QtGui, QtWidgets
from one import Ui_Dialog

# Creat app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hook Logik
def scan_port():
    mac = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993]
    host = input('Pls  enter text IP or name Domain: ')
    for port in mac:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((host, port))
        except socket.error:
            pass
        else:
            s.close
        print(host + ':' + str(port) + ' port active')
    scan = socket.socket(mac)
    domainO = ui.lineEdit.text()

    protokol = scan.scan_port(domainO)
    start = protokol.get_port()
    connect = start.get_connect('celsius')['temp']

    ui.label.setText(f' port active: {connect}')

ui.pushButton.clicked.connect(scan_port)

#mac = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993]
# host = input('Pls  enter text IP or name Domain: ')
# for port in mac:
#     s = socket.socket()
#     s.settimeout(1)
#     try:
#         s.connect((host, port))
#     except socket.error:
#         pass
#     else:
#         s.close
#         print(host + ':' + str(port) + ' port active')
# Main loop
sys.exit(app.exec_())