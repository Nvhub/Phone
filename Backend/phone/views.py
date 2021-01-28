from django.shortcuts import render,redirect
from .models import Persons
from .forms import PersonForm



def index(request):
    
    template_name = 'index.html'

    # Filter
    search = request.GET.get('search')
    if search:
        person = Persons.objects.filter(name__icontains = search)
    else:
        search = ''
        person = Persons.objects.all()

    context = { 'persons': person, 'search_value': search}
    return render(request, template_name, context)



def create(request): 

    template_name = "edit.html"
    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else: return redirect('/')

    context = {'form' : form}
    return render(request, template_name, context)


def delete(request, id):

    person = Persons.objects.get(id = id)
    
    if request.method == 'POST':
        person.delete()
        return redirect('/')
    
    template_name = 'delete.html'
    context = {'person': person}
    return render(request, template_name, context)


def edit(request, id):
    template_name = 'edit.html'
    person = Persons.objects.get(id = id)

    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/')
        else : return redirect('/')
    
    context = {'form':form,'person': person}

    return render(request, template_name, context)


def detail(request, id):
    template_name = 'contact-profile.html'
    person = Persons.objects.get(id = id)

    context = {'person': person}
    return render(request, template_name, context)

