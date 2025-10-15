from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.


def home(request):
    return render(request, "home.html")



def about(request):
    return render(request, "about.html")



def get_all(request):
    print("request",request)
    
    todo_list = Todo.objects.all().order_by("-creat_at")
    context = {
        "data": todo_list,
        "html_title" : "Items page"
    }
    return render(request, "home.html", context)



def get_data_by_id(request, id):
    print("request",request)
    
    todo_list = Todo.objects.get(id=id)
    
    context = {
        "items": todo_list,
        "html_title" : "View Items page"
    }
    return render(request, "view_items.html", context)





def create(request):
    
    if request.method == "POST":
        
         title = request.POST.get("name")
         describtion = request.POST.get("describtion")
         
         print(title, describtion)
         
         data = Todo(title=title, describtion=describtion)
         data.save()
         
         print("data is saved successfully")
         
        #  Todo.objects.create(title=title, describtion=describtion)
         
         return redirect("get-all")
    
    return render(request, "add_items.html")
    
    
    

def update(request, id):
    
    todo = Todo.objects.get(id=id)
    
    if request.method =="POST":
        
        title = request.POST.get("name")
        describtion = request.POST.get("describtion")
         
        todo.title = title
        todo.describtion = describtion
        todo.save()
        
        return redirect("get-all")
   

    context = {
        "id" : todo.id,
        "title": todo.title,
        "describtion": todo.describtion
    }

    return render(request, "edit_items.html", context)
    

    

def delete(request, id):
    todo = Todo.objects.get(id=id)

    todo.delete()

    return HttpResponse(f"{id} was deleted succesfully")

