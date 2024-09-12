import psutil
import os
import shutil
from datetime import datetime

class UsbManager:
    def __init__(self):
        self.usbDevices = []

        self.savingStatus = False

    def getUsbDevices(self):
        return self.usbDevices

    def getAvailableUsbDevices(self):
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
    
    def saveToUsbFile(self, text):
        with open(self.file_path, 'a') as file:
            file.write(text)
            file.write('\n')

    def startRecording(self, selected_mount_point):
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"log_file_{current_time}.txt"
        
        self.file_path = os.path.join(selected_mount_point, file_name)
        self.savingStatus = True

    def stopRecording(self):
        self.savingStatus = False

    def copyFileToUsb(self, file_path, selected_mount_point):
        try:
            shutil.copy2(file_path, selected_mount_point)  # shutil.copy2 preserves metadata
            print(f"File {file_path} copied to {selected_mount_point} successfully!")
        except Exception as e:
            print(f"Error while copying file: {e}")