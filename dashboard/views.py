from pyexpat.errors import messages
from django.shortcuts import render
from . forms import *
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,'dashboard/home.html')

def notes(request):
	if request.method == "POST":
		form = NotesForm(request.POST)
		if form.isvalid():
			notes = Notes(user=request.user,title=request.POST['title'],descripttion=request.POST['description'])
			notes.save()
		messages.success(request,f"Notes Added from {request.user.username} Successfully!")
	else:
			form=NotesForm()

	form = NotesForm()
	notes=Notes.objects.filter(user=request.user)
	context = {'notes':notes,'form':form}
	return render(request,'dashboard/notes.html')

def delete_note(request,pk=None):
	Notes.objects.get(id=pk)
	