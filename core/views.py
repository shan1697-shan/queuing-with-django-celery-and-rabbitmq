from django.shortcuts import render

from .forms import SendEmailForm
from core.tasks import send_email_task # we will define this function later


def index(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():            
            email = form.cleaned_data['email']
            send_email_task.delay(email)
            return render(request, 'index.html', {'form': form})
            

    form = SendEmailForm()
    return render(request, 'index.html', {'form': form})