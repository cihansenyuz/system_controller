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

    def copySwFileToUsb(self, file_path, selected_mount_point):
        try:
            destination_file_path = os.path.join(selected_mount_point, os.path.basename(file_path))
            if os.path.exists(destination_file_path):
                os.remove(destination_file_path)
                print(f"Existing file {destination_file_path} deleted.")

            print(f"File {file_path} copy started to {selected_mount_point}")
            shutil.copy2(file_path, selected_mount_point)  # shutil.copy2 preserves metadata
            print(f"File {file_path} copied to {selected_mount_point} successfully!")
            return True
        except Exception as e:
            print(f"Error while copying file: {e}")
            return False
        
    def unmountDeviceOnLinux(self, selected_mount_point):
        import subprocess
        print(f"Ejecting the device mounted at {selected_mount_point}")
        subprocess.run(['umount', selected_mount_point], check=True)
        print(f"Device ejected successfully!")

    '''def unmountDeviceOnWin(self, selected_mount_point):
        import win32file
        print(f"Ejecting the device mounted at {selected_mount_point}")
        drive_handle = win32file.CreateFile(selected_mount_point, win32file.GENERIC_READ, 
                                            win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE, None, 
                                            win32file.OPEN_EXISTING, 0, None)
        win32file.DeviceIoControl(drive_handle, win32file.IOCTL_STORAGE_EJECT_MEDIA, None, None)
        drive_handle.close()
        print(f"Device ejected successfully!")
    '''