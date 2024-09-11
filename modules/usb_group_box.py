from ui_compiled.ui_usb_group_box import Ui_usbGroupBox
from PySide6.QtWidgets import QGroupBox
from PySide6.QtCore import Signal

class UsbGroupBox(QGroupBox):
    savingStatusChanged = Signal(bool)

    def __init__(self, parentUsbManager, parentInfoMessages):
        super().__init__()
        self.ui = Ui_usbGroupBox()
        self.ui.setupUi(self)
        self.usbManager = parentUsbManager
        self.infoMessages = parentInfoMessages
        self.setTitle("USB Ayarları")

        self.ui.bitirButton.setEnabled(False)
        self.ui.bitirButton.setStyleSheet("color: gray;")

        self.savingStatusChanged.connect(self.onSavingStatusChanged)

        self.ui.kaydetButton.clicked.connect(self.onKaydetButtonClicked)
        self.ui.bitirButton.clicked.connect(self.onBitirButtonClicked)
        self.ui.usbPortYenileButton.clicked.connect(self.onUsbYenileButtonClicked)

        self.onUsbYenileButtonClicked() # Detect USB drives for the first time

    def onKaydetButtonClicked(self):
        self.selected_mount_point = self.ui.usbPortBox.currentText()
        if not self.selected_mount_point:
            self.infoMessages.appendPlainText("No USB drive selected!")
            return
        
        self.savingStatusChanged.emit(True)

    def onBitirButtonClicked(self):
        self.savingStatusChanged.emit(False)

    def onUsbYenileButtonClicked(self):
        self.ui.usbPortBox.clear()
        usbDeviceList = self.usbManager.getAvailableUsbDevices()
        if usbDeviceList:
            for device in usbDeviceList:
                self.ui.usbPortBox.addItem(device['mountpoint'])
        else:
            self.infoMessages.appendPlainText("No USB drives detected.")
        
        self.ui.usbPortBox.setCurrentIndex(-1)

    def onSavingStatusChanged(self, status):
        if(status):
            self.usbManager.startRecording(self.selected_mount_point)
            self.ui.kaydetButton.setEnabled(False)
            self.ui.kaydetButton.setStyleSheet("color: gray;")
            self.ui.bitirButton.setEnabled(True)
            self.ui.bitirButton.setStyleSheet("color: black;")
            self.infoMessages.appendPlainText("Log kaydı başlatıldı.")
        else:
            self.usbManager.stopRecording()
            self.ui.bitirButton.setEnabled(False)
            self.ui.bitirButton.setStyleSheet("color: gray;")
            self.ui.kaydetButton.setEnabled(True)
            self.ui.kaydetButton.setStyleSheet("color: black;")
            self.infoMessages.appendPlainText("Log kaydı durduruldu.")