from django.shortcuts import render, redirect
from .models import ContactMessages
from .forms import ContactMessagesForm
from django.utils import timezone



# Create your views here.
def contact(request):

    form = ContactMessagesForm(request.POST)
    control = request.user.is_authenticated

    context = {
        'form':form,
        'control':control,
    }
    if request.method == 'POST':
        if form.is_valid:
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")



            ContactMessages.objects.create(name=name, email=email, subject=subject, message=message  )
            return redirect('contact')

    return render(request, 'contact.html' , context)
