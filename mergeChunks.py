import os
import uuid
import shutil
import time
import random
from utils.FileUtils import FileUtils

#模拟临时生成文件夹名，避免重复可以使用uuid生成
FILE_PATH = "./files/"
#模拟前端传来的文件内容生成的Hash
FILE_HASH = "ebb115f3e2a43fe7b630ea44ba88daa0"
#模拟前端传来的最终切片合并的文件名
FILE_NAME = FILE_HASH + ".zip"
USER_NAME = "LNP"


#模拟收到合并切片请求
def handleMerge(tmpPath):
    files = FileUtils.GetAllFiles(tmpPath)

    # 合并切片 要注意合并的顺序
    def sortKey(fileName):
        return fileName.split("-")[1]

    files.sort(key=sortKey)
    with open(os.path.join(tmpPath, FILE_NAME), 'wb') as fp:
        for file in files:
            fp.write(open(file, 'rb').read())


#模拟前端传过来的文件切片，随机到达
def getChunkFiles():
    files = FileUtils.GetAllFiles(FILE_PATH)
    if len(files) - 1 < 0:
        return None
    index = random.randint(0, len(files) - 1)
    return files.pop(index)


# 模拟四个文件切片挨个到达
for i in range(4):
    file = getChunkFiles()
    if file is None:
        continue
    # tmpPath = os.path.join(
    #     "./", str(uuid.uuid3(uuid.NAMESPACE_DNS, USER_NAME + FILE_NAME)))

    # 前端传来file hash
    tmpPath = FILE_HASH
    # 替换文件切片的名称为 hash + “-” + 索引
    newFile = FILE_HASH + "-" + file.split("-")[1]
    if not os.path.exists(tmpPath):
        os.makedirs(tmpPath)
    shutil.move(file, os.path.join(tmpPath,newFile))
    #异步到达
    time.sleep(2)

# 动态计算文件夹(弃用，使用前端file hash)
# tmpPath = os.path.join(
#     "./", str(uuid.uuid3(uuid.NAMESPACE_DNS, USER_NAME + FILE_NAME)))

# 前端传来file hash
tmpPath = FILE_HASH
# 收到合并请求开始合并切片文件
handleMerge(tmpPath)

FileUtils.DeleteFile(tmpPath)
