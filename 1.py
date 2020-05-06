# if __name__ == "__main__":
import sys, pyowm
from PyQt5 import QtCore, QtGui, QtWidgets
# from one import Ui_Dialog

# Creat app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hook Logik
def get_weather_city():
    owm = pyowm.OWM('86df89ec9b32f70334257ad394766083')
    city = ui.lineEdit.text()

    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']

    ui.label.setText(f'Now Temp: {temperature}')

ui.pushButton.clicked.connect(get_weather_city)


# Main loop
sys.exit(app.exec_())