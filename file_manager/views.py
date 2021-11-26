from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import FileManagerForm
from .models import FileManager

@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == 'POST':
        form = FileManagerForm(request.POST, request.FILES)
        if form.is_valid():
	
            user = request.user
            name= request.POST.get('name')
            description= request.POST.get('description') 
            files= request.FILES.getlist('files') 
            for file in files:
                f = FileManager.objects.get_or_create(user= user,name=name,description=description, file=file), 
    
            return HttpResponse("Thanks for uploading file")
    else:
        form = FileManagerForm()
    return render(request, 'file_management.html', {'form': form})


@login_required(login_url='/accounts/login/')
def display_list(request):
	file_list = FileManager.objects.all()
	print(file_list)
	context ={
        'file_list':file_list,
    }
	return render(request,"file_list.html",context)