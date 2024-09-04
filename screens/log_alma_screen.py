from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import Signal, QByteArray, QRect
from ui_compiled.ui_log_alma_screen import Ui_logScreenWindow
from datetime import datetime
import dialogs.log_screen_dialogs as logScreendialogs
import platform
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

        self.createComboBoxes() # create lists and add them into comboboxes
        self.serialPort = QSerialPort()
        self.setDefaultSerialParameters() # set defaults
        self.getComPorts() # find available com ports and add them into combobox
        self.page = page
        self.saveLogs = False
        self.bitirButton.setEnabled(False)
        self.bitirButton.setStyleSheet("color: gray;")

        self.savingStatusChanged.connect(self.onSavingStatusChanged)
        self.serialPort.errorOccurred.connect(self.onErrorOccurred)# to handle occurred serial port errors
        self.serialPort.readyRead.connect(self.readFromSerialPort) # continuously read from serial port

        #### missing possible implementations ####
        # timing for read/write might need to be managed
        # errorOccured signal must be connected
        # disconnect button and closing the serial port may be considered
        # automaticly finding the com and selected

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
        self.create

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
        """
        A method to create comboBox contents

        Creates lists of serial port parameters, and adds them into related comboBoxes
        """
        # create lists
        self.baudRateList = ["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"]
        self.dataBitList = ["5 bits", "6 bits", "7 bits", "8 bits"]
        self.stopBitList = ["1 bit", "1.5 bits", "2 bits"]
        self.parityList = ["no parity", "even", "odd", "space", "mark"]
        self.flowControlList = ["no flow control", "hardware", "software"]
        #create command list
        self.commandList = ["Custar", "printenv"]

        # add lists to relative combo boxes
        self.baudRateBox.addItems(self.baudRateList)
        self.dataBitBox.addItems(self.dataBitList)
        self.stopBitBox.addItems(self.stopBitList)
        self.parityBox.addItems(self.parityList)
        self.flowControlBox.addItems(self.flowControlList)
        self.presetCommandBox.addItems(self.commandList)
        # set current selected items # to change default parameters, set indexes here
        self.baudRateBox.setCurrentIndex(7)
        self.dataBitBox.setCurrentIndex(3)
        self.stopBitBox.setCurrentIndex(0)
        self.parityBox.setCurrentIndex(0)
        self.flowControlBox.setCurrentIndex(0)
        self.presetCommandBox.setCurrentIndex(-1)

    def setPresetCommand(self):
        """
        This method is used for to set preset command
        """
        self.onPresetCommandBoxCurrentIndexChanged(self.presetCommandBox.currentIndex())

    def setDefaultSerialParameters(self):
        """
        A method to set current selected parameters for serial port

        Calls all slot methods to handle index changes in comboboxes to set serial port parameters as selected
        """
        self.onBaudRateBoxCurrentIndexChanged(self.baudRateBox.currentIndex())
        self.onDataBitBoxCurrentIndexChanged(self.dataBitBox.currentIndex())
        self.onStopBitBoxCurrentIndexChanged(self.stopBitBox.currentIndex())
        self.onParityBoxCurrentIndexChanged(self.parityBox.currentIndex())
        self.onFlowControlBoxCurrentIndexChanged(self.flowControlBox.currentIndex())
        self.infoMessages.clear()

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

        self.comPortBox.clear()
        if not self.comPortList:  # Check if the list is empty
            self.comPortBox.addItem("No Port Detected")
        else:
            for portInfo in self.comPortList:
                self.comPortBox.addItem(portInfo.portName())
        self.comPortBox.setCurrentIndex(-1)

    # slot function definitions
    def onBaudRateBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on baudRateBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
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
        self.infoMessages.appendPlainText("Info: Baud rate is set to " + str(self.serialPort.baudRate()))

    def onDataBitBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on dataBitBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
        if index == 0:
            self.serialPort.setDataBits(QSerialPort.DataBits.Data5)
        elif index == 1:
            self.serialPort.setDataBits(QSerialPort.DataBits.Data6)
        elif index == 2:
            self.serialPort.setDataBits(QSerialPort.DataBits.Data7)
        elif index == 3:
            self.serialPort.setDataBits(QSerialPort.DataBits.Data8)
        self.infoMessages.appendPlainText("Info: Data bits are set to " + str(self.serialPort.dataBits()))

    def onStopBitBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on stopBitBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
        if index == 0:
            self.serialPort.setStopBits(QSerialPort.StopBits.OneStop)
        elif index == 1:
            self.serialPort.setStopBits(QSerialPort.StopBits.OneAndHalfStop)
        elif index == 2:
            self.serialPort.setStopBits(QSerialPort.StopBits.TwoStop)
        self.infoMessages.appendPlainText("Info: Stop bit is set to " + str(self.serialPort.stopBits()))

    def onParityBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on parityBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
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
        self.infoMessages.appendPlainText("Info: Parity is set to " + str(self.serialPort.parity()))

    def onFlowControlBoxCurrentIndexChanged(self, index):
        """
        Slot method to handle item selection on flowControlBox

        Gets the index for selected item and sets it to serial port.

        Parameters:
        - index (int): index number of current item
        """
        if index == 0:
            self.serialPort.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
        elif index == 1:
            self.serialPort.setFlowControl(QSerialPort.FlowControl.HardwareControl)
        elif index == 2:
            self.serialPort.setFlowControl(QSerialPort.FlowControl.SoftwareControl)
        self.infoMessages.appendPlainText("Info: Flow control is set to " + str(self.serialPort.flowControl()))

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
        self.getComPorts()
        self.infoMessages.appendPlainText("Info: Available ports are refreshed.")
                                          
    def onConnectButtonClicked(self):
        """
        Slot method to handle click action on connectButton

        Refreshes available serial port list, and appends informative message to infoMessages

        """
        # match selected combobox item and comPortList item
        if len(self.comPortList) == 0:
            return
        for portInfo in self.comPortList:
            if portInfo.portName() == self.comPortBox.currentText():    # text vs text
                self.serialPort.setPort(portInfo)   # set port once matched item found
                self.serialPort.open(QSerialPort.ReadWrite) # open the port in read/write mode

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

    def readFromSerialPort(self):
        text = str(self.serialPort.readAll(), encoding="utf-8", errors="replace") # get bytes from serial, convert to str
        self.serialMessages.appendPlainText(text)                     # print them on UI
        
        if(self.saveLogs):
            self.saveToUsbFile(text)

    def onComPortButtonClicked(self):
        self.getComPorts()

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
        self.getComPorts()
        if self.page == 1:
            logScreendialogs.begin(self)
        else:
            pass # other pages

    def onErrorOccurred(self, error):
        """
        Method to handle errors for serial port

        Parameters:
        - error: raised error from the serial port

        """
        if error == QSerialPort.SerialPortError.OpenError:
            self.infoMessages.appendPlainText("Info: You have already opened the serial port.")
        elif error == QSerialPort.SerialPortError.DeviceNotFoundError:
            self.infoMessages.appendPlainText("Error: Attempting to open an non-existing device. Refresh port list.")
        elif error == QSerialPort.SerialPortError.PermissionError:
            self.infoMessages.appendPlainText("Error: Attempting to open an already opened device by another process or you don't have permissions")
        elif error == QSerialPort.SerialPortError.TimeoutError:
            self.infoMessages.appendPlainText("Error: A timeout error occurred, try again.")
        elif error == QSerialPort.SerialPortError.UnknownError:
            self.infoMessages.appendPlainText("Error: An unidentified error occurred, try again.")
        elif error == QSerialPort.SerialPortError.NoError:
            if self.serialPort.portName() == '':
                return
            else:
                self.infoMessages.appendPlainText("Info: Port " + (self.serialPort.portName()) + " is opened successfully!")

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.layoutWidget.setGeometry(QRect(0, 0, self.width(), self.height()))
        return super().resizeEvent(event)
    
    def findNewComPort(self):
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