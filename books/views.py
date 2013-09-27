# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from mysite.books.models import *
# Deprecated in Django 1.5. Use class-based views instead
# from django.views.generic.simple import direct_to_template

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q'].encode("utf-8")
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})

def objects_list(request, model):
    obj_list = model.objects.all()
    obj_name = model.__name__.lower() == 'author' and 'authors' or 'books'
    template_name = '%ss_list.html' % model.__name__.lower()
    return render(request, template_name, {obj_name: obj_list})

# def about_pages(request):
    # try:
    #     return direct_to_template(request, template="about/%s.html" % page)
    # except TemplateDoesNotExist:
    #     raise Http404
