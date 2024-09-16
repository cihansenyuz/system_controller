from PySide6.QtCore import QObject
import os
import shutil

class FileCacher(QObject):
    def __init__(self):
        super().__init__()
        print("FileCacher: Initialized")

    def cache(self, filePath, projectName):
        print(f"FileCacher: Entering cache function with filePath: {filePath}")
        os.makedirs("cache", exist_ok=True)
        cachedFilePath = os.path.join("cache", projectName, os.path.basename(filePath))
        
        if os.path.exists(cachedFilePath):
            if not self.isUpdated(cachedFilePath, filePath):
                print(f"FileCacher: File already cached and up-to-date. Exiting cache function, returning: {cachedFilePath}")
                return cachedFilePath

        try:
            shutil.copy2(filePath, cachedFilePath)
            print(f"FileCacher: File copied to cache. Exiting cache function, returning: {cachedFilePath}")
            return cachedFilePath
        except IOError:
            print("FileCacher: Exiting cache function, returning: None (IOError)")
            return None

    def isCached(self, fileName, projectName):
        print(f"FileCacher: Entering isCached function with fileName: {fileName}")
        cached_file_path = os.path.join("cache", projectName, fileName)
        
        if os.path.exists(cached_file_path):
            print(f"FileCacher: Exiting isCached function, returning: {cached_file_path}")
            return cached_file_path
        else:
            print("FileCacher: Exiting isCached function, returning: None")
            return None

    def isUpdated(self, localFilePath, remoteFilePath):
        print(f"FileCacher: Entering isUpdated function with localFilePath: {localFilePath}, remoteFilePath: {remoteFilePath}")
        local_last_modified_timestamp = os.path.getmtime(localFilePath)
        remote_last_modified_timestamp = os.path.getmtime(remoteFilePath)
        result = remote_last_modified_timestamp > local_last_modified_timestamp
        print(f"FileCacher: Exiting isUpdated function, returning: {result}")
        return result