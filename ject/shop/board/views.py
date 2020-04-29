from django.shortcuts import render, redirect
from board.models import Board
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.utils.http import urlquote
import os
# Create your views here.
UPLOAD_DIR="D:/upload"
def list(request):
    boardCount=Board.objects.count()
    boardList=Board.objects.all().order_by("-idx")
    return render(request, "list.html", {"boardList" : boardList, "boardCount" : boardCount})
def write(request):
    return render(request, "write.html")

@csrf_exempt
def insert(request):
    fname = ""
    fsize = 0
    if "file" in request.FILES:
        file=request.FILES["file"]
        fname = file.name
        fsize = file.size
        fp=open("%s%s" % (UPLOAD_DIR, fname), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
            fp.close()

    dto = Board( writer=request.POST["writer"],title=request.POST["title"], 
                 content=request.POST["content"], filename=fname,filesize=fsize )
    dto.save()
    print(dto)
    return redirect("/")
def download(request):
    id=request.GET['idx']
    dto=Board.objects.get(idx=id)
    path = UPLOAD_DIR+dto.filename
    print("path:",path)
    filename= os.path.basename(path)
    filename = filename.encode("utf-8")
    filename = urlquote(filename)
    print("pfilename:",os.path.basename(path))
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response["Content-Disposition"] = "attachment; filename*=UTF-8''{0}".format(filename)
        dto.down_up()
        dto.save()
        return response

def detail(request):
    id= request.GET['idx']
    dto=Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()
    
    print("filesize:",dto.filesize)
    filesize = "%.2f" % (dto.filesize/1024) 
    return render(request, "detail.html", {"dto": dto, "filesize":filesize, }) 
