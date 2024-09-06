from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget
from modules.serial_port import SerialPort
from modules.usb_manager import UsbManager
from PySide6.QtCore import Signal, QByteArray, QRect
from ui_compiled.ui_log_alma_screen import Ui_logScreenWindow
import dialogs.log_screen_dialogs as logScreendialogs
import time

#################################################################################
########## MODIFY onShowDialogsButtonClicked() if you inheret this class ########
#################################################################################

class LogScreenWindow(QWidget, Ui_logScreenWindow):
    savingStatusChanged = Signal(bool)

    def __init__(self, page):        
        super().__init__()
        self.setupUi(self)

        #Resize operations
        #self.layoutWidget.setGeometry(QRect(0, 0, self.width(), self.height()))
        
        self.serialPort = SerialPort(self)
        self.createComboBoxes() # create lists and add them into comboboxes
        self.page = page
        self.usbManager = UsbManager()
        self.bitirButton.setEnabled(False)
        self.bitirButton.setStyleSheet("color: gray;")

        self.savingStatusChanged.connect(self.onSavingStatusChanged)

        #### missing possible implementations ####
        # timing for read/write might need to be managed
        # errorOccured signal must be connected

        # button connections on log screen page
        self.logScreenBackButton.clicked.connect(self.onLogScreenBackButtonClicked)
        self.connectButton.clicked.connect(self.onConnectButtonClicked)
        self.sendButton.clicked.connect(self.onSendButtonClicked)
        self.comPortButton.clicked.connect(self.onResetButtonClicked)
        self.clearInfoPanelButton.clicked.connect(self.onClearInfoPanelButtonClicked)
        self.clearMessagePanelButton.clicked.connect(self.onClearMessagePanelButtonClicked)
        self.disconnectButton.clicked.connect(self.onDisconnectButtonClicked)
        self.showDialogsButton.clicked.connect(self.onShowDialogsButtonClicked)
        self.kaydetButton.clicked.connect(self.onKaydetButtonClicked)
        self.bitirButton.clicked.connect(self.onBitirButtonClicked)
        self.usbPortYenileButton.clicked.connect(self.onUsbYenileButtonClicked)
        self.mBootButton.clicked.connect(self.onMBootButtonClicked)

        # combobox connections on log screen page
        self.baudRateBox.currentIndexChanged.connect(self.onBaudRateBoxCurrentIndexChanged)
        self.dataBitBox.currentIndexChanged.connect(self.onDataBitBoxCurrentIndexChanged)
        self.stopBitBox.currentIndexChanged.connect(self.onStopBitBoxCurrentIndexChanged)
        self.parityBox.currentIndexChanged.connect(self.onParityBoxCurrentIndexChanged)
        self.flowControlBox.currentIndexChanged.connect(self.onFlowControlBoxCurrentIndexChanged)
        self.presetCommandBox.currentIndexChanged.connect(self.onPresetCommandBoxCurrentIndexChanged)

        self.onShowDialogsButtonClicked() # call it once the page is created
        self.onUsbYenileButtonClicked() # Detect USB drives

    def createComboBoxes(self):
        self.commandList = ["custar", "printenv"]

        self.baudRateBox.addItems(self.serialPort.baudRateList)
        self.dataBitBox.addItems(self.serialPort.dataBitList)
        self.stopBitBox.addItems(self.serialPort.stopBitList)
        self.parityBox.addItems(self.serialPort.parityList)
        self.flowControlBox.addItems(self.serialPort.flowControlList)
        self.presetCommandBox.addItems(self.commandList)

    def onBaudRateBoxCurrentIndexChanged(self, index):
        self.serialPort.setNewBaudRate(index)
        self.infoMessages.appendPlainText("Info: Baud rate is set to " + str(self.serialPort.baudRate()))

    def onDataBitBoxCurrentIndexChanged(self, index):
        self.serialPort.setNewDataBits(index)
        self.infoMessages.appendPlainText("Info: Data bits are set to " + str(self.serialPort.dataBits()))

    def onStopBitBoxCurrentIndexChanged(self, index):
        self.serialPort.setNewStopBits(index)
        self.infoMessages.appendPlainText("Info: Stop bit is set to " + str(self.serialPort.stopBits()))

    def onParityBoxCurrentIndexChanged(self, index):
        self.serialPort.setNewParity(index)
        self.infoMessages.appendPlainText("Info: Parity is set to " + str(self.serialPort.parity()))

    def onFlowControlBoxCurrentIndexChanged(self, index):
        self.serialPort.setNewFlowControl(index)
        self.infoMessages.appendPlainText("Info: Flow control is set to " + str(self.serialPort.flowControl()))

    def onLogScreenBackButtonClicked(self):
        self.parent().setCurrentIndex(0)

    def onResetButtonClicked(self):
        self.serialPort.getComPorts()
        self.infoMessages.appendPlainText("Info: Available ports are refreshed.")
                                          
    def onConnectButtonClicked(self):
        # match selected combobox item and comPortList item
        if len(self.serialPort.comPortList) == 0:
            return
        for portInfo in self.serialPort.comPortList:
            if portInfo.portName() == self.comPortBox.currentText():    # text vs text
                self.serialPort.setPort(portInfo)   # set port once matched item found
                self.serialPort.open(SerialPort.ReadWrite) # open the port in read/write mode

    def onMBootButtonClicked(self):
        text = "reset"                                      # restarts the TV
        bytes = QByteArray(text.encode())                   # convert str to byte       
        self.serialPort.write(bytes)                        # write it to serial port
        time.sleep(1)                                       # waits 1 second

        i=0
        for i in range(100):                                     # tries to get mboot
            text = "\r"                                           # empty to simulate alone Entry
            bytes = QByteArray(text.encode())                   # convert str to byte
            self.serialPort.write(bytes)                        # write it to serial port
            time.sleep(0.1)                                     # waits 0.1 second

    def onPresetCommandBoxCurrentIndexChanged(self,index):
        self.messageLine.setText(self.commandList[index])

    def onSendButtonClicked(self):
        text = self.messageLine.text()
        self.serialMessages.appendPlainText(">> "+ text)
        if(self.usbManager.savingStatus):
            try:
                self.usbManager.saveToUsbFile(">> "+ text)
            except Exception as e:
                self.infoMessages.appendPlainText(f"An error occurred while saving the file: {e}")
        self.messageLine.clear()

        bytes = QByteArray(text.encode())                   # convert str to byte
        self.serialPort.write(bytes)                        # write it to serial port

    def onDisconnectButtonClicked(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            self.infoMessages.appendPlainText("Info: Port " + self.serialPort.portName() + " is closed.")
        else:
            self.infoMessages.appendPlainText("Info: No serial port is open or already closed")

    def onComPortButtonClicked(self):
        self.serialPort.getComPorts()

    def onClearInfoPanelButtonClicked(self):
        self.infoMessages.clear()

    def onClearMessagePanelButtonClicked(self):
        self.serialMessages.clear()

    def onShowDialogsButtonClicked(self):
        self.serialPort.getComPorts()
        if self.page == 1:
            logScreendialogs.begin(self)
        else:
            pass # other pages

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.layoutWidget.setGeometry(QRect(0, 0, self.width(), self.height()))
        return super().resizeEvent(event)

    def onKaydetButtonClicked(self):
            self.selected_mount_point = self.usbPortBox.currentText()
            if not self.selected_mount_point:
                self.infoMessages.appendPlainText("No USB drive selected!")
                return
            
            self.savingStatusChanged.emit(True)

    def onBitirButtonClicked(self):
        self.savingStatusChanged.emit(False)

    def onUsbYenileButtonClicked(self):
        self.usbPortBox.clear()
        usbDeviceList = self.usbManager.getAvailableUsbDevices()
        if usbDeviceList:
            for device in usbDeviceList:
                self.usbPortBox.addItem(device['mountpoint'])
        else:
            self.infoMessages.appendPlainText("No USB drives detected.")
        
        self.usbPortBox.setCurrentIndex(-1)

    def onSavingStatusChanged(self, status):
        if(status):
            self.usbManager.startRecording(self.selected_mount_point)
            self.kaydetButton.setEnabled(False)
            self.kaydetButton.setStyleSheet("color: gray;")
            self.bitirButton.setEnabled(True)
            self.bitirButton.setStyleSheet("color: black;")
            self.infoMessages.appendPlainText("Log kaydı başlatıldı.")
        else:
            self.usbManager.stopRecording()
            self.bitirButton.setEnabled(False)
            self.bitirButton.setStyleSheet("color: gray;")
            self.kaydetButton.setEnabled(True)
            self.kaydetButton.setStyleSheet("color: black;")
            self.infoMessages.appendPlainText("Log kaydı durduruldu.")