from django.shortcuts import render, HttpResponseRedirect
from .forms import ImageForm
from .models import Image
from django.urls import reverse

# Create your views here.


def home(request):
	form = ImageForm()
	context = {'form':form}
	return render(request, 'home.html', context)


def images(request):
  form = ImageForm()
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      new_entry = Image()
      new_entry.name = form.cleaned_data['name']
      new_entry.image = form.cleaned_data['image']
      new_entry.save()
    else:
      print('error', form.errors)
  else:
    pass
  return HttpResponseRedirect(reverse('home'))

 
 