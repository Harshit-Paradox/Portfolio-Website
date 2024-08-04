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


# def Contact(request):
#     if request.method == "POST":
#       data = request.POST

#       name = data.get('name')
#       email= data.get('email')
#       message = data.get('message')

     
#       Contact.objects.create(
#         message=message,
#         email=email,
#         name= name,
#         )
      
#       return redirect('/contact')
#     queryset = Contact.objects.all()
#     context = {'contact': queryset}

    
#     messages.success(request, "We will contact you shortly")
#     return render(request, 'index.html',context)



# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})

# def success_view(request):
#     messages.success(request, "We will contact you shortly")
#     return render(request, 'index.html')

# Create your views here.
