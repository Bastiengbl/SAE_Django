from django.shortcuts import render,redirect,get_object_or_404
from computerApp import models 
from computerApp.models import Machine
from computerApp.models import Personnel
from .forms import AddMachineForm
def index(request) :
    
    context = {}
    return render(request, 'index.html', context)

def machine_list_view(request) :
  machines = Machine.objects.all()
  context={'machines': machines} 
  return render(request,
    'computerapp/machine_list.html',
     context)


def personnes_list_view(request) :
    persos = Personnel.objects.all()
    context={'persos': persos}
    return render(request,
     'computerapp/personnes_list.html',
     context)

def machine_detail_view(request, pk):
  machine = get_object_or_404(Machine, id=pk)
  context={'machine': machine}
  return render(request,
   'computerapp/machine_detail.html',
   context)
     
def personnes_detail_view(request, pk):
  personne = get_object_or_404(Personnel, num_secu=pk)
  context={'personne': personne}
  return render(request,
   'computerapp/personne_detail.html',
   context)

def machine_add_form(request):
  if request.method == 'POST':
    form = AddMachineForm(request.POST or None)
    if form.is_valid():
      new_machine = Machine(nom=form.cleaned_data['nom'])
      new_machine.save()
      return redirect('machines')
  else:
    form = AddMachineForm()
    context = {'form': form}
    return render(request,
     'computerapp/machine_add.html',context)

def about(request) :
    
    context = {}
    return render(request, 'computerapp/about.html', context)