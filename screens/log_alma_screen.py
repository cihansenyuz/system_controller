from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget
from modules.serial_port import SerialPort
from PySide6.QtCore import Signal, QByteArray, QRect
from ui_compiled.ui_log_alma_screen import Ui_logScreenWindow
from datetime import datetime
import dialogs.log_screen_dialogs as logScreendialogs
import psutil
import os
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
        self.saveLogs = False
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
        self.baudRateBox.currentIndexChanged.connect(self.serialPort.onBaudRateBoxCurrentIndexChanged)
        self.dataBitBox.currentIndexChanged.connect(self.serialPort.onDataBitBoxCurrentIndexChanged)
        self.stopBitBox.currentIndexChanged.connect(self.serialPort.onStopBitBoxCurrentIndexChanged)
        self.parityBox.currentIndexChanged.connect(self.serialPort.onParityBoxCurrentIndexChanged)
        self.flowControlBox.currentIndexChanged.connect(self.serialPort.onFlowControlBoxCurrentIndexChanged)
        self.presetCommandBox.currentIndexChanged.connect(self.onPresetCommandBoxCurrentIndexChanged)

        self.onShowDialogsButtonClicked() # call it once the page is created
        self.onUsbYenileButtonClicked() # Detect USB drives

    def createComboBoxes(self):
        """
        A method to create comboBox contents

        Creates lists of serial port parameters, and adds them into related comboBoxes
        """

        self.commandList = ["custar", "printenv"]

        # add lists to relative combo boxes
        self.baudRateBox.addItems(self.serialPort.baudRateList)
        self.dataBitBox.addItems(self.serialPort.dataBitList)
        self.stopBitBox.addItems(self.serialPort.stopBitList)
        self.parityBox.addItems(self.serialPort.parityList)
        self.flowControlBox.addItems(self.serialPort.flowControlList)
        self.presetCommandBox.addItems(self.commandList)

    def onLogScreenBackButtonClicked(self):
        """
        Slot method to handle click action on logScreenBackButton

        Sets the page of main screen as current page

        """
        self.parent().setCurrentIndex(0)

    def onResetButtonClicked(self):
        """
        Slot method to handle click action on resetButton

        Refreshes available serial port list, and appends informative message to infoMessages

        """
        self.serialPort.getComPorts()
        self.infoMessages.appendPlainText("Info: Available ports are refreshed.")
                                          
    def onConnectButtonClicked(self):
        """
        Slot method to handle click action on connectButton

        Refreshes available serial port list, and appends informative message to infoMessages

        """
        # match selected combobox item and comPortList item
        if len(self.serialPort.comPortList) == 0:
            return
        for portInfo in self.serialPort.comPortList:
            if portInfo.portName() == self.comPortBox.currentText():    # text vs text
                self.serialPort.setPort(portInfo)   # set port once matched item found
                self.serialPort.open(SerialPort.ReadWrite) # open the port in read/write mode

    def onMBootButtonClicked(self):
        """
        To get the TV to the Mboot Menu
        """
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
        """
        To set selected preset command
        """

        self.messageLine.setText(self.commandList[index])


    def onSendButtonClicked(self):
        """
        Slot method to handle click action on sendButton

        Takes the user input in messageLine, and writes it to the serial port

        """
        text = self.messageLine.text()
        self.serialMessages.appendPlainText(">> "+ text)
        if(self.saveLogs):
            self.saveToUsbFile(">> "+ text)
        self.messageLine.clear()

        bytes = QByteArray(text.encode())                   # convert str to byte
        self.serialPort.write(bytes)                        # write it to serial port

    def onDisconnectButtonClicked(self):
        """
        Slot method to handle click action on disconnectButton

        Closes serial ports if there is open one, and appends related message to infoMessages

        """
        if self.serialPort.isOpen():
            self.serialPort.close()
            self.infoMessages.appendPlainText("Info: Port " + self.serialPort.portName() + " is closed.")
        else:
            self.infoMessages.appendPlainText("Info: No serial port is open or already closed")

    '''def readFromSerialPort(self):
        text = str(self.serialPort.readAll(), encoding="utf-8", errors="replace") # get bytes from serial, convert to str
        self.serialMessages.appendPlainText(text)                     # print them on UI
        
        if(self.saveLogs):
            self.saveToUsbFile(text)'''

    def onComPortButtonClicked(self):
        self.serialPort.getComPorts()

    def onClearInfoPanelButtonClicked(self):
        """
        Slot method to handle click action on clearInfoPanelButton

        Clears all message history in the infoMessages

        """
        self.infoMessages.clear()

    def onClearMessagePanelButtonClicked(self):
        """
        Slot method to handle click action on clearMessagePanelButton

        Clears all message history in the serialMessages

        """
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
    
    def findNewComPort(self):
        # get a list of port names
        oldComPortList = []
        for port in self.serialPort.comPortList:
            oldComPortList.append(port.portName())
        # refresh the port list
        self.serialPort.getComPorts()
        # compare if newPort is in the old list or not
        for newPort in self.serialPort.comPortList:
            if oldComPortList.count(newPort.portName()):
                pass
            else:
                self.comPortBox.setCurrentText(newPort.portName())
                self.infoMessages.appendPlainText("Info: Port " + (newPort.portName()) + " is found.")
        if self.comPortBox.currentIndex() == -1:
            self.infoMessages.appendPlainText("Error: No new device is found!\nClick 'Show Dialogs' button and follow instructions again.")

    def get_usb_drives(self):
        """
        Function to detect mounted USB drives.
        """
        partitions = psutil.disk_partitions(all=False)  # 'all=True' can show unmounted devices
        usb_drives = []

        for partition in partitions:
            # Use 'removable' in partition.opts for Windows and other OS checks
            if 'removable' in partition.opts or '/media/' in partition.mountpoint or '/mnt/' in partition.mountpoint:
                usb_drives.append({
                    'device': partition.device,
                    'mountpoint': partition.mountpoint,
                    'fstype': partition.fstype
                })

        return usb_drives

    def onKaydetButtonClicked(self):
            selected_mount_point = self.usbPortBox.currentText()
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"log_file_{current_time}.txt"

            if not selected_mount_point:
                self.infoMessages.appendPlainText("No USB drive selected!")
                return

            self.file_path = os.path.join(selected_mount_point, file_name)
            self.savingStatusChanged.emit(True)

    def saveToUsbFile(self, text):
        try:
            with open(self.file_path, 'a') as file:
                file.write(text)
                file.write('\n')

        except Exception as e:
            self.infoMessages.appendPlainText(f"An error occurred while saving the file: {e}")

    def onBitirButtonClicked(self):
        self.savingStatusChanged.emit(False)

    def onUsbYenileButtonClicked(self):
        self.usbPortBox.clear()
        usb_drives = self.get_usb_drives()
        if usb_drives:
            for drive in usb_drives:
                self.usbPortBox.addItem(drive['mountpoint'])
        else:
            self.infoMessages.appendPlainText("No USB drives detected.")
        
        self.usbPortBox.setCurrentIndex(-1)

    def onSavingStatusChanged(self, status):
        if(status):
            self.saveLogs = True
            self.kaydetButton.setEnabled(False)
            self.kaydetButton.setStyleSheet("color: gray;")
            self.bitirButton.setEnabled(True)
            self.bitirButton.setStyleSheet("color: black;")
            self.infoMessages.appendPlainText("Log kaydı başlatıldı.")
        else:
            self.saveLogs = False
            self.bitirButton.setEnabled(False)
            self.bitirButton.setStyleSheet("color: gray;")
            self.kaydetButton.setEnabled(True)
            self.kaydetButton.setStyleSheet("color: black;")
            self.infoMessages.appendPlainText("Log kaydı durduruldu.")