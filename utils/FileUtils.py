import os
import uuid
import shutil
import time


# 文件处理相关
class FileUtils:
    """
    删除文件
        删除供文件
        :filePath 要删除的文件路径
    """
    @staticmethod
    def DeleteFile(filePath):
        if os.path.exists(filePath):
            print("delete %s" % filePath)
            os.remove(filePath)
        else:
            print("no this file")

    """
    获取指定文件夹下所有文件
        dirPath: 文件夹路径
    """

    @staticmethod
    def GetAllFiles(dirPath):
        allFiles = []
        fileList = os.listdir(dirPath)
        for file in fileList:
            fullFilePath = os.path.join(dirPath, file)
            if os.path.isdir(fullFilePath):
                allFiles += FileUtils.GetAllFiles(fullFilePath)
            else:
                # 文件
                allFiles.append(fullFilePath)
        return allFiles
