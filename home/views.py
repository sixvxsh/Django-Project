from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm,TodoUpateForm

# Create your views here.
def home(request):
    all = Todo.objects.all()
    return render(request , 'home.html', {'todos': all})


# def say_hello(request):
#     return render(request,'hello.html', context={'name': 'midia'})

def detail(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request,'detail.html' , {'todo':todo})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'todo deleted successfuly', extra_tags='success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        #this line is for validation 
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #first title,body,created are for model the seconds are for form
            Todo.objects.create(title=cd['title'],body=cd['body'], created=cd['created'])
            messages.success(request , 'Todo created successfully' , 'success')
            return redirect('home')
    else:
        form=TodoCreateForm()
    return render(request ,'create.html',{'form':form})


def update(request , todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'todo updated successfuly', 'success')
            return redirect('details', todo_id )
    else:
        #for get method
        form = TodoUpateForm(instance=todo)
    return render(request , 'update.html', {'form':form})