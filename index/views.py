from django.shortcuts import render
from .models import about, slider, client, Musician
from index import forms

# Create your views here.
def home(request):
    
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    
    context = {
        'about' : aboutdata,
        'slider' : sliderdata,
        'client' : clientdata
    }
    
    return render(request, 'index.html', context)

def aboutus(request):
    musician_list = Musician.objects.order_by('first_name')
    musician_table_data = {
        'musician' : musician_list,
        'heading' : 'This is a list of Musicians'
    }
    
    new_form = forms.MusicianForm()
    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        
        if new_form.is_valid():
            new_form.save(commit=True)
        
    context = {
        'musician_table_data' : musician_table_data,
        'test_form' : new_form,
        'heading1' : 'Add New Musician'
        
    }
    
    
    return render(request, 'about.html', context)
