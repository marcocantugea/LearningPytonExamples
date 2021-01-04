# Clase para manipular archivos localmente usando rutas relativas
# Version 0.0.1
# Author Marco Cantu Gea

from pathlib import Path


class LocalStorage:

    def __init__(self, pathName, fileName=None):
        self.pathName = pathName
        self.PathObj = Path(pathName)
        self.fileName=fileName

    def setPathName(self, pathName):
        self.PathObj = Path(pathName)
        self.pathName = pathName
        return self

    def getPathName(self=None):
        return self.pathName

    def exist(self):
        return self.PathObj.exists()

    def makeDir(self):
        if len(self.pathName)>=3:
            self.PathObj.mkdir()

        return self

    def removeDir(self):
        if len(self.pathName)>=3:
            self.PathObj.rmdir()
            self.pathName = ""
            self.PathObj = None

        return self

    def getPathContent(self, arg='*.*'):
        return self.PathObj.glob(arg)

    def searchFileInPath(self, fileName=None):
        foundFile = fileName is None and self.fileName or fileName
        return self.getPathContent(foundFile)


localstorage = LocalStorage("./testfolder")
print(localstorage.exist())
if not localstorage.exist():
    localstorage.makeDir()
    if localstorage.exist():
        print("path created")
elif localstorage.exist():
    localstorage.removeDir()
    print("path removed")

#si existe obtener el contenido del path
localstorage.setPathName("../ecommerce")
if localstorage.exist():
    for item in localstorage.getPathContent():
        print(item)

items =localstorage.searchFileInPath("shipping.py")
for file in items:
    print(f"file found:{file}")