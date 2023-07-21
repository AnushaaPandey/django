from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Blog
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