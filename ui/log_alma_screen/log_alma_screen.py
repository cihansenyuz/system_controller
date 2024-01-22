from PySide6.QtWidgets import QWidget
from ui.log_alma_screen.ui_log_alma_screen import Ui_logScreenWindow
from ui.log_alma_screen.serial_port import SerialPort

class logScreenWindow(QWidget, Ui_logScreenWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createComboBoxes() # create lists and add them into comboboxes
        self.setDefaultSerialParameters()
        self.serialPort = SerialPort()

        self.logScreenBackButton.clicked.connect(self.onLogScreenBackButtonClicked)

        self.baudRateBox.currentIndexChanged.connect(self.onBaudRateBoxCurrentIndexChanged)
        self.dataBitBox.currentIndexChanged.connect(self.onDataBitBoxCurrentIndexChanged)
        self.stopBitBox.currentIndexChanged.connect(self.onStopBitBoxCurrentIndexChanged)
        self.parityBox.currentIndexChanged.connect(self.onParityBoxCurrentIndexChanged)
        self.flowControlBox.currentIndexChanged.connect(self.onFlowControlBoxCurrentIndexChanged)


    def createComboBoxes(self):
        self.baudRateList = ["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"]
        self.dataBitList = ["5 bits", "6 bits", "7 bits", "8 bits"]
        self.stopBitList = ["1 bit", "1.5 bits", "2 bits"]
        self.parityList = ["no parity", "even", "odd", "space", "mark"]
        self.flowControlList = ["no flow control", "hardware", "software"]
        
        self.baudRateBox.addItems(self.baudRateList)
        self.dataBitBox.addItems(self.dataBitList)
        self.stopBitBox.addItems(self.stopBitList)
        self.parityBox.addItems(self.parityList)
        self.flowControlBox.addItems(self.flowControlList)

    def setDefaultSerialParameters(self):
        self.baudRateBox.setCurrentIndex(3)
        self.dataBitBox.setCurrentIndex(3)
        self.stopBitBox.setCurrentIndex(0)
        self.parityBox.setCurrentIndex(0)
        self.flowControlBox.setCurrentIndex(0)


    def onBaudRateBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.setBaudRate(SerialPort.QSerialPort.BaudRate.Baud1200)
        elif index == 1:
            self.setBaudRate(SerialPort.QSerialPort.BaudRate.Baud2400)
        elif index == 2:
            self.setBaudRate(SerialPort.QSerialPort.BaudRate.Baud4800)
        elif index == 3:
            self.setBaudRate(SerialPort.QSerialPort.BaudRate.Baud9600)
        elif index == 4:
            self.setBaudRate(SerialPort.QSerialPort.BaudRate.Baud19200)
        elif index == 5:
            self.setBaudRate(SerialPort.QSerialPort.BaudRate.Baud38400)
        elif index == 6:
            self.setBaudRate(SerialPort.QSerialPort.BaudRate.Baud57600)
        elif index == 7:
            self.setBaudRate(SerialPort.QSerialPort.BaudRate.Baud115200)
        print("Baud rate is set: ", self.baudRate())

    def onDataBitBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.setDataBits(SerialPort.QSerialPort.DataBits.Data5)
        elif index == 1:
            self.setDataBits(SerialPort.QSerialPort.DataBits.Data6)
        elif index == 2:
            self.setDataBits(SerialPort.QSerialPort.DataBits.Data7)
        elif index == 3:
            self.setDataBits(SerialPort.QSerialPort.DataBits.Data8)
        print("Data bits are set: ", self.dataBits())

    def onStopBitBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.setStopBits(SerialPort.QSerialPort.StopBits.OneStop)
        elif index == 1:
            self.setStopBits(SerialPort.QSerialPort.StopBits.OneAndHalfStop)
        elif index == 2:
            self.setStopBits(SerialPort.QSerialPort.StopBits.TwoStop)
        print("Stop bit is set: ", self.stopBits())

    def onParityBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.setParity(SerialPort.QSerialPort.Parity.NoParity)
        elif index == 1:
            self.setParity(SerialPort.QSerialPort.Parity.EvenParity)
        elif index == 2:
            self.setParity(SerialPort.QSerialPort.Parity.OddParity)
        elif index == 3:
            self.setParity(SerialPort.QSerialPort.Parity.SpaceParity)
        elif index == 4:
            self.setParity(SerialPort.QSerialPort.Parity.MarkParity)
        print("Parity is set: ", self.parity())

    def onFlowControlBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.setFlowControl(SerialPort.QSerialPort.FlowControl.NoFlowControl)
        elif index == 1:
            self.setFlowControl(SerialPort.QSerialPort.FlowControl.HardwareControl)
        elif index == 2:
            self.setFlowControl(SerialPort.QSerialPort.FlowControl.SoftwareControl)
        print("Flow control is set: ", self.flowControl())


    def onLogScreenBackButtonClicked(self):
        self.parent().setCurrentIndex(0)