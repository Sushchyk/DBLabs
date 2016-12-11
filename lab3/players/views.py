from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .dbmanager import DatabaseManager


db = DatabaseManager()
countOfTeamsOnPage = 100

def index(request):
    return render(request, 'players/index.html')


def teams(request, num = "1"):
    if request.method == 'POST':
        #TODO ADD CACHE HERE
        team_name = request.POST['team_name'].lower()
        teams_ = db.findTeamsByName(team_name)
        search_info = ''
        return render(request, 'players/showteams.html',
                      {'response': {'teams': teams_, 'search_info': search_info, 'search_phrase': request.POST['team_name']}})

    num = int(num)
    countOfPages = db.getCountOfTeams() / countOfTeamsOnPage + 1
    teams_ = db.getTeams(countOfTeamsOnPage, (num - 1) * countOfTeamsOnPage)
    pages = []
    if (num < 5 or num > countOfPages - 4):
        pages = [1, 2, 3, 4, 5, -1, countOfPages - 4, countOfPages - 3, countOfPages -2, countOfPages - 1, countOfPages]
    else:
        pages = [1, 2, -1, num - 1, num, num + 1, -1,  countOfPages - 1, countOfPages]

    return render(request, 'players/showteams.html',
                  {'response': {'teams': teams_ , "number": num, 'pages': pages }})

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


def deleteTeam(request):
    if request.method == "POST":
        if request.POST["deleted_team"] != "":
            db.deleteTeam(request.POST["deleted_team"])
        return HttpResponseRedirect('/players/teams')