from django.shortcuts import render, redirect 
from django.db.models import Q, Count
from .models import League, Team, Player


from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
        "leagues":League.objects.filter(sport="Baseball"),
        "w_leagues":League.objects.filter(name__contains="womens"),
        "leagues_hockey":League.objects.filter(sport__contains="Hockey"),
        "nofut_leagues":League.objects.exclude(sport="Football"),
        "conf_league":League.objects.filter(name__contains="Conference"),
        "atlantic_league": League.objects.filter(name__contains="Atlantic"),
        "dallas_league": Team.objects.filter(location__contains="Dallas"),
        "rapt_team": Team.objects.filter(team_name__contains="Raptors"),
        "city_team" : Team.objects.filter(location__contains="City"),
        "starT_team": Team.objects.filter(team_name__startswith="T"),
        "location_team": Team.objects.all().order_by("location"),
        "inv_ord": Team.objects.all().order_by("-team_name"),
        "last_name": Player.objects.filter(last_name="Cooper"),
        "first_name": Player.objects.filter(first_name="Joshua"),
        "cooperexcjoshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
        "AlexOR": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")).order_by('first_name', "last_name"),
        
  
  
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")