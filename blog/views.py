from django.shortcuts import render

def index(requests):
    return render(
        request,
        'blog/index.html',
    )

# Create your views here.
