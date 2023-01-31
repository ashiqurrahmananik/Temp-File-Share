from django.shortcuts import render
from .models import myfile

# Create your views here.
def index(request):
    return render (request,'index.html')
def upload(request):
    if request.method == 'POST':
        userfile = request.FILES['formfile']
        print(userfile)
        newfile = myfile(uploadfile = userfile)
        newfile.save()
        return render (request,'download.html',{'new_url': str(newfile.uploadfile.url)})
