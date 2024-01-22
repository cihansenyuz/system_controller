from PySide6.QtSerialPort import QSerialPort

class SerialPort(QSerialPort):
    def __init__(self, ui):
        super().__init__()

        self.createComboBoxes(ui) # create lists and add them into comboboxes
        self.setDefaultSerialParameters(ui)

        ui.baudRateBox.currentIndexChanged.connect(self.onBaudRateBoxCurrentIndexChanged)
        ui.dataBitBox.currentIndexChanged.connect(self.onDataBitBoxCurrentIndexChanged)
        ui.stopBitBox.currentIndexChanged.connect(self.onStopBitBoxCurrentIndexChanged)
        ui.parityBox.currentIndexChanged.connect(self.onParityBoxCurrentIndexChanged)
        ui.flowControlBox.currentIndexChanged.connect(self.onFlowControlBoxCurrentIndexChanged)
        
    def createComboBoxes(self, ui):
        self.baudRateList = ["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"]
        self.dataBitList = ["5 bits", "6 bits", "7 bits", "8 bits"]
        self.stopBitList = ["1 bit", "1.5 bits", "2 bits"]
        self.parityList = ["no parity", "even", "odd", "space", "mark"]
        self.flowControlList = ["no flow control", "hardware", "software"]
        
        ui.baudRateBox.addItems(self.baudRateList)
        ui.dataBitBox.addItems(self.dataBitList)
        ui.stopBitBox.addItems(self.stopBitList)
        ui.parityBox.addItems(self.parityList)
        ui.flowControlBox.addItems(self.flowControlList)

    def setDefaultSerialParameters(self, ui):
        ui.baudRateBox.setCurrentIndex(3)
        ui.dataBitBox.setCurrentIndex(3);
        ui.stopBitBox.setCurrentIndex(0);
        ui.parityBox.setCurrentIndex(0);
        ui.flowControlBox.setCurrentIndex(0);

    def onBaudRateBoxCurrentIndexChanged(self, index):
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
        print("Baud rate is set: ", self.baudRate())

    def onDataBitBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.setDataBits(QSerialPort.DataBits.Data5)
        elif index == 1:
            self.setDataBits(QSerialPort.DataBits.Data6)
        elif index == 2:
            self.setDataBits(QSerialPort.DataBits.Data7)
        elif index == 3:
            self.setDataBits(QSerialPort.DataBits.Data8)
        print("Data bits are set: ", self.dataBits())

    def onStopBitBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.setStopBits(QSerialPort.StopBits.OneStop)
        elif index == 1:
            self.setStopBits(QSerialPort.StopBits.OneAndHalfStop)
        elif index == 2:
            self.setStopBits(QSerialPort.StopBits.TwoStop)
        print("Stop bit is set: ", self.stopBits())

    def onParityBoxCurrentIndexChanged(self, index):
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
        print("Parity is set: ", self.parity())

    def onFlowControlBoxCurrentIndexChanged(self, index):
        if index == 0:
            self.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
        elif index == 1:
            self.setFlowControl(QSerialPort.FlowControl.HardwareControl)
        elif index == 2:
            self.setFlowControl(QSerialPort.FlowControl.SoftwareControl)
        print("Flow control is set: ", self.flowControl())
