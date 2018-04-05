from django.shortcuts import render

# Create your views here.

import datetime
from django.http import HttpResponse
from comics.ComicProgram import *


def index(request):
    return render(request, 'comics/home.html')


def comicslist(request):
    cp = ComicProgram()
    cL = cp.createComicList()
    showlist = []

    for x in cL:
        showlist.append(str(x))
        


    c = {
        'comiclist': showlist
    }

    return render(request, 'comics/comiclist.html', c)


def comicsinfo(request,name):
    cp = ComicProgram()
    cL = cp.createComicList()
    c = cp.getComic(name)
    vList = c.getVolList()
    showlist = []
    for x in vList:
        showlist.append(str(x))

    c = {
        'volumnlist': showlist,
        'comicname': name
    }
    return render(request, 'comics/comicinfo.html', c)

def comicspage(request, comicname, volname, pagenumber=0):
    vol = Volumn(comicname, volname)
    data = vol.getPageData(pagenumber)

    #return render(request, "comics/comicpage.html", c)

    return HttpResponse(data, content_type="image")

def comicsview(request, comicname, volname, pagenumber):

    pagenumber = int(pagenumber)
    vol = Volumn(comicname, volname)
    prevpagenumber = 0
    nextpagenumber = 0
    if pagenumber<=0:
        prevpagenumber = 0
        nextpagenumber = 1
    elif pagenumber>vol.numberOfPages():
        prevpagenumber = vol.numberOfPages() - 2
        nextpagenumber = vol.numberOfPages() - 1
    else:
        prevpagenumber = pagenumber - 1
        nextpagenumber = pagenumber + 1


    width = None
    height = None
    width, height = vol.getPageSize(pagenumber)
    Ax = None
    Ay = None
    if width != None:
        Ax = width/3
    if height != None:
        Ay = height/10

    c = {
        "pagelist": vol.getPagesList(),
        "comicname": comicname,
        "volname": volname,
        "pagenumber": pagenumber,
        "prevpagenumber": prevpagenumber,
        "nextpagenumber": nextpagenumber,
        "width": width,
        "height": height,
        #"Ax":Ax,
        #"Ay":Ay,
        #"Bx":width,
        #"By":height

    }
    return render(request, "comics/comicview2.html", c)



def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)