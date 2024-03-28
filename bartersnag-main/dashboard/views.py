from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from barter.models import Barter

@login_required
def index(request):
    barters = Barter.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'barters': barters,
    })

