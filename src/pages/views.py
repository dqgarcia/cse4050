from django.http import HttpResponse
from django.shortcuts import render
from .forms import postForm
from .models import post


# Create your views here.
def home_view(request, *args, **kwargs):
    obj = post.objects.all()
    context = {
        'posts': obj
    }
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def post_create_view(request):
	form = postForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'form' : form
	}
	return render(request, "create.html", context)