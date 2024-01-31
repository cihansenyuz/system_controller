from PySide6.QtWidgets import QWidget
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QByteArray, SIGNAL, SLOT
from ui.log_alma_screen.ui_log_alma_screen import Ui_logScreenWindow

import platform

class logScreenWindow(QWidget, Ui_logScreenWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createComboBoxes() # create lists and add them into comboboxes
        self.serialPort = QSerialPort()
        self.setDefaultSerialParameters() # set defaults
        self.getComPorts() # find available com ports and add them into combobox
        
        self.serialPort.readyRead.connect(self.readFromSerialPort) # continuously read from serial port

        #### missing possible implementations ####
        # timing for read/write might need to be managed
        # errorOccured signal must be connected
        # disconnect button and closing the serial port may be considered

        # button connections on log screen page
        self.logScreenBackButton.clicked.connect(self.onLogScreenBackButtonClicked)
        self.connectButton.clicked.connect(self.onConnectButtonClicked)
        self.send_button.clicked.connect(self.onSendButtonClicked)
        self.comPortButton.clicked.connect(self.onResetButtonClicked)
        self.clearPanelsButton.clicked.connect(self.onClearPanelsButtonClicked)
        # combobox connections on log screen page
        self.baudRateBox.currentIndexChanged.connect(self.onBaudRateBoxCurrentIndexChanged)
        self.dataBitBox.currentIndexChanged.connect(self.onDataBitBoxCurrentIndexChanged)
        self.stopBitBox.currentIndexChanged.connect(self.onStopBitBoxCurrentIndexChanged)
        self.parityBox.currentIndexChanged.connect(self.onParityBoxCurrentIndexChanged)
        self.flowControlBox.currentIndexChanged.connect(self.onFlowControlBoxCurrentIndexChanged) 

    def createComboBoxes(self):
        # create lists
        self.baudRateList = ["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"]
        self.dataBitList = ["5 bits", "6 bits", "7 bits", "8 bits"]
        self.stopBitList = ["1 bit", "1.5 bits", "2 bits"]
        self.parityList = ["no parity", "even", "odd", "space", "mark"]
        self.flowControlList = ["no flow control", "hardware", "software"]
        # add lists to relative combo boxes
        self.baudRateBox.addItems(self.baudRateList)
        self.dataBitBox.addItems(self.dataBitList)
        self.stopBitBox.addItems(self.stopBitList)
        self.parityBox.addItems(self.parityList)
        self.flowControlBox.addItems(self.flowControlList)
        # set current selected items # to change default parameters, set indexes here
        self.baudRateBox.setCurrentIndex(7)
        self.dataBitBox.setCurrentIndex(3)
        self.stopBitBox.setCurrentIndex(0)
        self.parityBox.setCurrentIndex(0)
        self.flowControlBox.setCurrentIndex(0)

    def setDefaultSerialParameters(self):
        self.onBaudRateBoxCurrentIndexChanged(self.baudRateBox.currentIndex())
        self.onDataBitBoxCurrentIndexChanged(self.dataBitBox.currentIndex())
        self.onStopBitBoxCurrentIndexChanged(self.stopBitBox.currentIndex())
        self.onParityBoxCurrentIndexChanged(self.parityBox.currentIndex())
        self.onFlowControlBoxCurrentIndexChanged(self.flowControlBox.currentIndex())

    def getComPorts(self):
        if platform.system() == 'Windows':
            self.comPortList = QSerialPortInfo.availablePorts()
        else:
            self.comPortListAll = QSerialPortInfo.availablePorts()
            self.comPortList = list()
            for port in self.comPortListAll:
                if port.portName().find("USB") != -1:
                    self.comPortList.append(port)
        
        self.comPortBox.clear()
        if not self.comPortList:  # Check if the list is empty
            self.comPortBox.addItem("No Port Detected")
        else:
            for portInfo in self.comPortList:
                self.comPortBox.addItem(portInfo.portName())

    # slot function definitions
    def onBaudRateBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud1200)
        elif index == 1:
            self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud2400)
        elif index == 2:
            self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud4800)
        elif index == 3:
            self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud9600)
        elif index == 4:
            self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud19200)
        elif index == 5:
            self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud38400)
        elif index == 6:
            self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud57600)
        elif index == 7:
            self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud115200)
        print("Baud rate is set: ", self.serialPort.baudRate())

    def onDataBitBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.serialPort.setDataBits(QSerialPort.DataBits.Data5)
        elif index == 1:
            self.serialPort.setDataBits(QSerialPort.DataBits.Data6)
        elif index == 2:
            self.serialPort.setDataBits(QSerialPort.DataBits.Data7)
        elif index == 3:
            self.serialPort.setDataBits(QSerialPort.DataBits.Data8)
        print("Data bits are set: ", self.serialPort.dataBits())

    def onStopBitBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.serialPort.setStopBits(QSerialPort.StopBits.OneStop)
        elif index == 1:
            self.serialPort.setStopBits(QSerialPort.StopBits.OneAndHalfStop)
        elif index == 2:
            self.serialPort.setStopBits(QSerialPort.StopBits.TwoStop)
        print("Stop bit is set: ", self.serialPort.stopBits())

    def onParityBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.serialPort.setParity(QSerialPort.Parity.NoParity)
        elif index == 1:
            self.serialPort.setParity(QSerialPort.Parity.EvenParity)
        elif index == 2:
            self.serialPort.setParity(QSerialPort.Parity.OddParity)
        elif index == 3:
            self.serialPort.setParity(QSerialPort.Parity.SpaceParity)
        elif index == 4:
            self.serialPort.setParity(QSerialPort.Parity.MarkParity)
        print("Parity is set: ", self.serialPort.parity())

    def onFlowControlBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.serialPort.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
        elif index == 1:
            self.serialPort.setFlowControl(QSerialPort.FlowControl.HardwareControl)
        elif index == 2:
            self.serialPort.setFlowControl(QSerialPort.FlowControl.SoftwareControl)
        print("Flow control is set: ", self.serialPort.flowControl())

    def onLogScreenBackButtonClicked(self):
        self.parent().setCurrentIndex(0)

    def onResetButtonClicked(self):
        self.getComPorts()

    def onConnectButtonClicked(self):
        # match selected combobox item and comPortList item
        connectedFlag = 0
        for portInfo in self.comPortList:
            if portInfo.portName() == self.comPortBox.currentText():    # text vs text
                self.serialPort.setPort(portInfo)   # set port once matched item found
                connectedFlag = 1
                break
        if not connectedFlag:
            self.infoMessages.appendPlainText("Error: Selected port cannot be found! Please refresh port list")
            return
        
        # open the port in read/write mode
        portOpenFlag = self.serialPort.open(QSerialPort.ReadWrite)
        if portOpenFlag:
            self.infoMessages.appendPlainText("Info: Selected port is now open")
        else:
            self.infoMessages.appendPlainText("Error: cannot open selected port")

    def onSendButtonClicked(self):
        text = self.message_line.text()                     # get the string
        self.serialMessages.appendPlainText(">> "+ text)    # print it on UI
        self.message_line.clear()                           # clear the message line

        bytes = QByteArray(text.encode())                   # convert str to byte
        self.serialPort.write(bytes)                        # write it to serial port

    def readFromSerialPort(self):
            text = str(self.serialPort.readAll(), encoding="utf-8", errors="replace") # get bytes from serial, convert to str
            self.serialMessages.appendPlainText(text)                     # print them on UI

    def onComPortButtonClicked(self):
        self.getComPorts()

    def onClearPanelsButtonClicked(self):
        self.serialMessages.clear()
        self.infoMessages.clear()