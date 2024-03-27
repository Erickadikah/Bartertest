from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewBarterForm
from .models import Category, Barter


# Create your views here.
def info(request, pk):
    barter = get_object_or_404(Barter, pk=pk)
    related_barters = Barter.objects.filter(category=barter.category, is_exchanged=False).exclude(pk=pk)[0:3]

    return render(request, 'barter/info.html', {
        'barter': barter,
        'related_barters': related_barters
    })
    
    
@login_required
def new(request):
    if request.method == 'POST':
        form = NewBarterForm(request.POST, request.FILES)

        if form.is_valid():
            barter = form.save(commit=False)
            barter.created_by = request.user
            barter.save()

            return redirect('barter:info', pk=barter.id)
    else:
        form = NewBarterForm()

    return render(request, 'barter/form.html', {
        'form': form,
        'title': 'New barter',
    })

