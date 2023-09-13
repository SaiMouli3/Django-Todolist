from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .models import Todo

def index(request):
    return HttpResponse("Hello")


def entry(request):
    all_lists = Todo.objects.all()
    context = {'all_lists': all_lists}
    return render(request ,'todolist/entry.html',context)




def manual(request):
    if request.method == 'POST':
        title_text = request.POST.get('title_text')
        desc_text =  request.POST.get('desc_text')
        comp_text =  request.POST.get('comp_text')

        todo = Todo(title = title_text,description=desc_text,completed =comp_text )
        todo.save()
        return redirect('entry')



    return render(request, 'todolist/manual.html')

