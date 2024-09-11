from ui_compiled.ui_usb_group_box import Ui_usbGroupBox
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

class UsbGroupBox(QWidget, Ui_usbGroupBox):
    savingStatusChanged = Signal(bool)

    def __init__(self, usbManager, infoMessages):
        super().__init__()
        self.setupUi(self)
        self.usbManager = usbManager
        self.infoMessages = infoMessages

        self.bitirButton.setEnabled(False)
        self.bitirButton.setStyleSheet("color: gray;")

        self.savingStatusChanged.connect(self.onSavingStatusChanged)

        self.kaydetButton.clicked.connect(self.onKaydetButtonClicked)
        self.bitirButton.clicked.connect(self.onBitirButtonClicked)
        self.usbPortYenileButton.clicked.connect(self.onUsbYenileButtonClicked)

        self.onUsbYenileButtonClicked() # Detect USB drives

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