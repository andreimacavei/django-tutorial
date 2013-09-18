from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from mysite.contact.forms import ContactForm

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
            url = "?email=" + cd['email']
            return HttpResponseRedirect('/contact/thanks/' + url)
    else:
        form = ContactForm(
            # initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})

def success(request):
    if request.method == 'GET' and request.GET:
        email = request.GET['email']
    elif request.method == 'POST':
        email = request.POST['email']
    else:
        return HttpResponseRedirect('/contact/')
    return render(request, 'contact_success.html', {'email': email})
