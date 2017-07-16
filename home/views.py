from django.shortcuts import render
from home.models import Home

def home(request):
    context = {
        'dados_home': Home.objects.get(ativo=1),
    }

    return render(request, 'home/index.html', context)
