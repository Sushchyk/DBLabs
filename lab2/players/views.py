from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .dbmanager import DatabaseManager

db = DatabaseManager()

def index(request):
    return render(request, 'players/index.html')

def teams(request):
    teams_ = db.getAllTeams()
    return render(request, 'players/showteams.html',  {'response': {'teams': teams_ }})

def countries(request):
    countries_ = db.getAllCountries()
    return render(request, 'players/showcountries.html',  {'response': {'countries': countries_ }})

def createPlayer(request):
    teams_ = db.getAllTeams()
    countries_ = db.getAllCountries()
    positions_ = db.getAllPositions()
    return render(request, 'players/addplayer.html', {'response': {'positions': positions_, 'teams': teams_, 'countries': countries_}})

def storePlayer(request):
    if request.method == "POST":
        if request.POST["country"] != "" and request.POST["team"] != "":
            db.insertPlayer(request.POST)
        return HttpResponseRedirect('/players')

def editPlayer(request):
    if request.method == "POST":
        if request.POST["player"] != "":
            teams_ = db.getAllTeams()
            countries_ = db.getAllCountries()
            player = db.getPlayerById(request.POST['player'])
            positions_ = db.getAllPositions()
            return render(request, 'players/editplayer.html',
                          {'response': {'positions': positions_, 'teams': teams_, 'countries': countries_, 'player': player}})

    return HttpResponseRedirect('/players')


def deletePlayer(request):
    if request.method == "POST":
        if request.POST["deleted_player"] != "":
            db.deletePlayer(request.POST["deleted_player"])
        return HttpResponseRedirect('/players')


def showPlayers(request):
    teams_ = db.getAllTeams()
    countries_ = db.getAllCountries()
    players_ = db.getAllPlayers()
    sum_by_country_ = db.sumByCountry()
    sum_by_team_ = db.sumByTeam()
    count_of_player_by_pos = db.countOfByPlayersByPositions()
    return render(request, 'players/showplayers.html', {'response':
        {'sum_of_players_by_position': count_of_player_by_pos,'sum_by_country': sum_by_country_,
        'sum_by_team': sum_by_team_, 'countries': countries_, 'players': players_}})


def updatePlayer(request):
    if request.method == "POST":
        if request.POST["edited_player"] != "":
            db.editPlayer(request.POST)
    return HttpResponseRedirect('/players')


