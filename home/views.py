from django.shortcuts import render
from home.models import Home, ComoFunciona, Duvida
from django.core.exceptions import ObjectDoesNotExist as DoesNotExist


def home(request):
    """ método principal """
    try:
        dados_home = Home.objects.get(ativo=1)
    except DoesNotExist:
        dados_home = False

    como_funciona = ComoFunciona.objects.filter(ativo=1)

    if request.method == 'POST':
        duvida = Duvida()
        duvida.nome = request.POST.get('nome')
        duvida.email = request.POST.get('email')
        duvida.celular = request.POST.get('celular')
        duvida.mensagem = request.POST.get('mensagem')
        duvida.save()

    context = {
        'dados_home': dados_home,
        'como_funciona': como_funciona,
    }

    return render(request, 'home/index.html', context)
