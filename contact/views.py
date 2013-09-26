from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from mysite.contact.forms import ContactForm
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['andrei.macavei@eaudeweb.ro'],
            )
            messages.success(request, "Your email is {}".format(cd['email']))
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            # initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})

def success(request):
    return render(request, 'contact_success.html')
