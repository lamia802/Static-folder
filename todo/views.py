from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
# Create your views here.


def get_all(request):
    print("request",request)
    
    todo_list = Todo.objects.all().order_by("-creat_at")
    if todo_list:

        print(todo_list)
        
        for q in todo_list:
            print("id", q.id)
            print("titile", q.title)
            print("describtion", q.describtion)

        output = ",".join([q.describtion for q in todo_list])
        return HttpResponse(output)
    else:
        return HttpResponse(f"Not available hhsd data")




def create(request):
    Todo.objects.create()

def update(request, id, title, describtion):
    
    todo = Todo.objects.get(id=id)

    todo.title = title
    todo.describtion = describtion
    todo.save()

    return HttpResponse(f"{todo.title} and {todo.describtion} updated")
    

    

def delete(request, id):
    todo = Todo.objects.get(id=id)

    todo.delete()

    return HttpResponse(f"{id} was deleted succesfully")



def about(request):
    return HttpResponse("this is about page")