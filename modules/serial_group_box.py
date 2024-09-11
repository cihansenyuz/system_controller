from ui_compiled.ui_serial_group_box import Ui_serialGroupBox
from PySide6.QtWidgets import QGroupBox
from PySide6.QtCore import Slot

class SerialGroupBox(QGroupBox):
    def __init__(self, parentSerialPort, parentInfoMessages):
        super().__init__()
        self.ui = Ui_serialGroupBox()
        self.ui.setupUi(self)

        self.serialPort = parentSerialPort
        self.infoMessages = parentInfoMessages
        self.setTitle("Seri Port Seçimi")

        # Connect signals
        self.serialPort.portListUpdated.connect(self.updateComPortBox)
        self.serialPort.errorOccurred.connect(self.displayError)

        self.ui.connectButton.clicked.connect(self.onConnectButtonClicked)
        self.ui.refreshComButton.clicked.connect(self.onRefreshComButtonClicked)
        self.ui.disconnectButton.clicked.connect(self.onDisconnectButtonClicked)

    @Slot(list)
    def updateComPortBox(self, port_list):
        self.ui.comPortBox.clear()
        for portName in port_list:
                self.ui.comPortBox.addItem(portName)
        self.ui.comPortBox.setCurrentIndex(-1)

    @Slot(str)
    def displayError(self, error_message):
        self.infoMessages.appendPlainText(error_message)

    def onRefreshComButtonClicked(self):
        self.serialPort.getComPorts()
        self.infoMessages.appendPlainText("Info: Available ports are refreshed.")
                                          
    def onConnectButtonClicked(self):
        # match selected combobox item and comPortList item
        if len(self.serialPort.comPortList) == 0:
            return
        for portInfo in self.serialPort.comPortList:
            if portInfo.portName() == self.ui.comPortBox.currentText():    # text vs text
                self.serialPort.setPort(portInfo)   # set port once matched item found
                self.serialPort.open(self.serialPort.ReadWrite) # open the port in read/write mode

    def onDisconnectButtonClicked(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            self.infoMessages.appendPlainText("Info: Port " + self.serialPort.portName() + " is closed.")
        else:
            self.infoMessages.appendPlainText("Info: No serial port is open or already closed")