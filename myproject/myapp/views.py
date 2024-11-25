from django.shortcuts import render, redirect
from .forms import TeamForm
from .models import Team

def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.user = request.user
            team.save()
            return redirect('view_teams')
    else:
        form = TeamForm()
    return render(request, 'myapp/add_team.html', {'form': form})

from django.shortcuts import render
from .models import Team

def view_teams(request):
    teams = Team.objects.all()  # Получаем все команды
    return render(request, 'myapp/view_teams.html', {'teams': teams})



def set_cookie(request):
    response = HttpResponse("Настройки сохранены")
    response.set_cookie('theme', 'dark')
    response.set_cookie('language', 'ru')
    return response

def get_cookie(request):
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'en')
    return render(request, 'myapp/cookies.html', {'theme': theme, 'language': language})
