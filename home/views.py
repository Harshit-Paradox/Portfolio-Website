from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages
from .form import ContactForm



def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the same page or another after saving
    return render(request, 'index.html', {'form': form})



def index(request):
    return render(request, 'index.html')