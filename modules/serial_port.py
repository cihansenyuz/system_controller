from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QObject
import platform

class SerialPort(QSerialPort):
    def __init__(self, parent: QObject = None):
        super().__init__(parent)

        self.setDefaultSerialParameters()
        self.getComPorts()

        # create lists
        self.baudRateList = ["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"]
        self.dataBitList = ["5 bits", "6 bits", "7 bits", "8 bits"]
        self.stopBitList = ["1 bit", "1.5 bits", "2 bits"]
        self.parityList = ["no parity", "even", "odd", "space", "mark"]
        self.flowControlList = ["no flow control", "hardware", "software"]

        self.errorOccurred.connect(self.onErrorOccurred)# to handle occurred serial port errors
        self.readyRead.connect(self.readFromSerialPort) # continuously read from serial port

    def setDefaultSerialParameters(self):
        """
        A method to set current selected parameters for serial port

        Sets serial port parameters as default
        """
        self.setBaudRate(QSerialPort.BaudRate.Baud115200)
        self.setDataBits(QSerialPort.DataBits.Data8)
        self.setStopBits(QSerialPort.StopBits.OneStop)
        self.setParity(QSerialPort.Parity.NoParity)
        self.setFlowControl(QSerialPort.FlowControl.NoFlowControl)

    def getComPorts(self):
        """
        A method to get available serial ports to user for selection

        Calls all slot methods to handle index changes in comboboxes to set serial port parameters as selected
        """
        if platform.system() == 'Windows':
            self.comPortList = QSerialPortInfo.availablePorts()
        else:
            self.comPortListAll = QSerialPortInfo.availablePorts()
            self.comPortList = list()
            for port in self.comPortListAll:
                if port.portName().find("USB") != -1:
                    self.comPortList.append(port)

        self.parent().comPortBox.clear()
        if not self.comPortList:  # Check if the list is empty
            self.parent().comPortBox.addItem("No Port Detected")
        else:
            for portInfo in self.comPortList:
                self.parent().comPortBox.addItem(portInfo.portName())
        self.parent().comPortBox.setCurrentIndex(-1)

    def onErrorOccurred(self, error):
        """
        Method to handle errors for serial port

        Parameters:
        - error: raised error from the serial port

        """
        if error == QSerialPort.SerialPortError.OpenError:
            self.parent().infoMessages.appendPlainText("Info: You have already opened the serial port.")
        elif error == QSerialPort.SerialPortError.DeviceNotFoundError:
            self.parent().infoMessages.appendPlainText("Error: Attempting to open an non-existing device. Refresh port list.")
        elif error == QSerialPort.SerialPortError.PermissionError:
            self.parent().infoMessages.appendPlainText("Error: Attempting to open an already opened device by another process or you don't have permissions")
        elif error == QSerialPort.SerialPortError.TimeoutError:
            self.parent().infoMessages.appendPlainText("Error: A timeout error occurred, try again.")
        elif error == QSerialPort.SerialPortError.UnknownError:
            self.parent().infoMessages.appendPlainText("Error: An unidentified error occurred, try again.")
        elif error == QSerialPort.SerialPortError.NoError:
            if self.portName() == '':
                return
            else:
                self.parent().infoMessages.appendPlainText("Info: Port " + (self.portName()) + " is opened successfully!")

    def readFromSerialPort(self):
        text = str(self.readAll(), encoding="utf-8", errors="replace") # get bytes from serial, convert to str
        self.parent().serialMessages.appendPlainText(text)                     # print them on UI
        
        if(self.parent().saveLogs):
            self.saveToUsbFile(text)


    def onBaudRateBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on baudRateBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
        if index == 0:
            self.setBaudRate(QSerialPort.BaudRate.Baud1200)
        elif index == 1:
            self.setBaudRate(QSerialPort.BaudRate.Baud2400)
        elif index == 2:
            self.setBaudRate(QSerialPort.BaudRate.Baud4800)
        elif index == 3:
            self.setBaudRate(QSerialPort.BaudRate.Baud9600)
        elif index == 4:
            self.setBaudRate(QSerialPort.BaudRate.Baud19200)
        elif index == 5:
            self.setBaudRate(QSerialPort.BaudRate.Baud38400)
        elif index == 6:
            self.setBaudRate(QSerialPort.BaudRate.Baud57600)
        elif index == 7:
            self.setBaudRate(QSerialPort.BaudRate.Baud115200)
        self.parent().infoMessages.appendPlainText("Info: Baud rate is set to " + str(self.baudRate()))

    def onDataBitBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on dataBitBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
        if index == 0:
            self.setDataBits(QSerialPort.DataBits.Data5)
        elif index == 1:
            self.setDataBits(QSerialPort.DataBits.Data6)
        elif index == 2:
            self.setDataBits(QSerialPort.DataBits.Data7)
        elif index == 3:
            self.setDataBits(QSerialPort.DataBits.Data8)
        self.parent().infoMessages.appendPlainText("Info: Data bits are set to " + str(self.dataBits()))

    def onStopBitBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on stopBitBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
        if index == 0:
            self.setStopBits(QSerialPort.StopBits.OneStop)
        elif index == 1:
            self.setStopBits(QSerialPort.StopBits.OneAndHalfStop)
        elif index == 2:
            self.setStopBits(QSerialPort.StopBits.TwoStop)
        self.parent().infoMessages.appendPlainText("Info: Stop bit is set to " + str(self.stopBits()))

    def onParityBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on parityBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
        if index == 0:
            self.setParity(QSerialPort.Parity.NoParity)
        elif index == 1:
            self.setParity(QSerialPort.Parity.EvenParity)
        elif index == 2:
            self.setParity(QSerialPort.Parity.OddParity)
        elif index == 3:
            self.setParity(QSerialPort.Parity.SpaceParity)
        elif index == 4:
            self.setParity(QSerialPort.Parity.MarkParity)
        self.parent().infoMessages.appendPlainText("Info: Parity is set to " + str(self.parity()))

    def onFlowControlBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on flowControlBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
        if index == 0:
            self.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
        elif index == 1:
            self.setFlowControl(QSerialPort.FlowControl.HardwareControl)
        elif index == 2:
            self.setFlowControl(QSerialPort.FlowControl.SoftwareControl)
        self.parent().infoMessages.appendPlainText("Info: Flow control is set to " + str(self.flowControl()))


    def getNewComPortName(self):
        # get a list of port names
        oldComPortList = []
        for port in self.comPortList:
            oldComPortList.append(port.portName())
        # refresh the port list
        self.getComPorts()
        # compare if newPort is in the old list or not
        for newPort in self.comPortList:
            if oldComPortList.count(newPort.portName()):
                pass
            else:
                return newPort.portName()
