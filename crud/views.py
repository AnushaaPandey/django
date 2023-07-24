from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Blog , Contact
from .forms import forms
from .forms import BlogForm

# Create your views here.
def homepage(request):
    blog = Blog.objects.all()
    print(blog)
    return render(request,"crud/index.html", {"Blogs": blog})

def create(request):
    forms = BlogForm(request.POST or None)
    if(forms.is_valid()):
        forms.save()
        return redirect("home")
    return render(request, "crud/create.html", {"forms": forms})

def particularData(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "crud/index.html", {"blog":blog})

def contacts(request):
    if(request.method=="POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        crud = Contact(
            name = name,
            email= email,
            message = message
        )
        crud.save()
    return render(request,"crud/contacts.html" )

def Delete(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == 'POST':
        blog.delete
        return redirect("home")
    return render(request, "crud/contacts.html", {"blog":blog})


