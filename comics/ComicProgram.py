import sys
import os
import zipfile
from PIL import Image




DEFAULTPATH = os.path.abspath(os.path.dirname(os.getcwd())) + "/comics/comictest/img"
PATHLIST = [DEFAULTPATH]



class Volumn:
    def __init__(self,comicname, volname, path=DEFAULTPATH):
        self.number = 0
        self.comicname = comicname
        self.volname = volname
        self.vpath = DEFAULTPATH + '/' + comicname + '/' + volname
        self.pathList = PATHLIST
        self.isdir = os.path.isdir(self.vpath)
        self.iszip = os.path.splitext(self.vpath)[1] == ".zip"
        self.zfile = None
        if self.iszip:
            self.zfile = zipfile.ZipFile(self.vpath, 'r')







    def getPagesList(self):
        if self.isdir:
            pageslist = os.listdir(self.vpath)
            l = []
            for x in pageslist:
                l.append(self.vpath + '/' + x)
            return l
        elif self.iszip:
            l = []
            for x in self.zfile.namelist():
                #x = x.encode('cp437')
                #x = x.decode('utf8')
                if ".jpg" in x or ".png" in x:
                    l.append(x)
            print(l)
            return l
        print("getPagesList: Not a directory or a zipfile")
        return None




    def numberOfPages(self):
        return len(self.getPagesList())


    def getPagePath(self, number):
        number = int(number)
        l = self.getPagesList()
        if number<0:
            return l[0]
        elif number>len(l):
            return l[-1]
        return l[number]

    def getPageData(self, number):
        number = int(number)

        if self.isdir:
            path = self.getPagePath(number)
            print("isdir"+path)

            pagedata = open(path, "rb").read()
            return pagedata
        elif self.iszip:
            namelist = self.getPagesList()
            pagedata = self.zfile.read(namelist[number])

            return pagedata

        print("getPageData: Not a directory or a zipfile")
        return None

    def getPageSize(self, number):
        if self.isdir:
            pagepath = self.getPagePath(number)
            im = Image.open(pagepath)
            x, y = im.size

            print(x, y)
            return x, y
        elif self.iszip:
            print(' ', number, ' ', self.getPagePath(number))
            zimg = self.zfile.open(self.getPagePath(number))
            print(zimg,' ',number,' ',self.getPagePath(number))
            im = Image.open(zimg)
            x, y = im.size
            print(x,' ',y)
            return x, y
        else:
            return None, None

class Comic:
    def __init__(self, path):
        self.path = path
        print("path ",path)
        self.name = path.split('/')[-1]
        print(self.name)
        self.volname = []

    def __str__(self):
        return self.name

    def getPageList(self, volname):

        return(os.listdir(self.path + "/" + self.name + "/" + volname))

    def setPath(self,path):
        self.path = path


    def getVolList(self):
        print("path ",self.path)
        return(os.listdir(self.path))

    def getName(self):
        return self.name



class ComicProgram:
    def __init__(self):

        self.pathList = PATHLIST
        self.comicName = []
        self.comicList = []
        self.comicMap = {}

    def createComicList(self):
        self.comicList = []

        for l in self.pathList: #all paths including comics
            p = os.listdir(l)
            for comic in p:
                comicp = l + '/' + comic
                if os.path.isdir(comicp):
                    self.comicList.append(Comic(comicp))

        return self.comicList









    def getComic(self, name):
        for c in self.comicList:
            if c.getName() == name:
                return c
        return None
    


cp = ComicProgram()
cp.createComicList()


