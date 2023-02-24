from django.shortcuts import render, HttpResponse
from datetime import datetime
from base.models import Contact
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# from django.http import

# Create your views here.


def index(request):
    context = {
        # we send fetch data, with given name
        'variable': "this is a Var"
    }
    return render(request, 'index.html', context)
    # return HttpResponse('Home Page')


def about(request):
    return render(request, 'about.html')


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        print('inside if')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        print(name)
        contact = Contact(name=name, email=email,
                          number=number, date=datetime.today())
        contact.save()
        messages.success(request, 'Form Filled Successfully')
    elif request.method == 'GET':
        print('outside ')
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')
