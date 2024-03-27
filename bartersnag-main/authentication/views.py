from django.shortcuts import render, redirect
from barter.models import Category, Barter

from .forms import SignupForm

def index(request):
    barters = Barter.objects.filter(is_exchanged=False)[0:4]
    categories = Category.objects.all()
    
    return render(request, 'authentication/index.html',{
        'categories': categories,
        'barters': barters,
    })
    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'authentication/signup.html', {
        'form': form
    })
