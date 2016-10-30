from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.code import Code
from bson.son import SON
from data import *
from random import randint
class DatabaseManager:

    def __init__(self):
            self.client = MongoClient()
            self.db = self.client.lab3

    def fillDb(self):
            self.db.insert('')

    def getAllTeams(self):
        teams = [team for team in self.db.teams.find().limit(100)] # Return list of teams
        for team in teams:
            team['found_year'] = int(team['found_year'])
        return teams

    def getTeams(self, limit_, skip_):
        teams = [team for team in self.db.teams.find().limit(limit_).skip(skip_)]  # Return list of teams
        for team in teams:
            team['found_year'] = int(team['found_year'])
        return teams

    def getCountOfTeams(self):
        return self.db.teams.find().count()

    def getAllCountries(self):
        countries = [country for country in self.db.countries.find()]  # Return list of countries
        for c in countries:
            c['number_of_people'] = int(c['number_of_people'])
        return countries

    def getAllPositions(self):
        positions = [position for position in self.db.positions.find()]  # Return list of countries
        return positions

    def insertPlayer(self, dict):
        team = self.db.teams.find_one({'_id': ObjectId(dict['team'])})
        country = self.db.countries.find_one({'_id': ObjectId(dict['country'])})
        positions = [];
        print ', '.join(positions)
        for position in dict.getlist('positions'):
            newPosition = self.db.positions.find_one({'_id': ObjectId(position)})
            positions.append(newPosition)
        player = {'name': dict['name'],'number': dict['number'], 'position': positions,
                 'team': team, 'country': country, 'price': int(dict['price'])}
        self.db.players.insert(player)

    def getAllPlayers(self):
        players = [player for player in self.db.players.find()]  # Return list of players
        for player in players:
            player['number'] = int(player['number'])
        return players

    def deletePlayer(self, id):
        self.db.players.delete_one({'_id': ObjectId(id)})

    def getPlayerById(self, id):
        player =  self.db.players.find_one({'_id': ObjectId(id)})
        print player['name']
        print player['position']
        print player['number']
        return player

    def editPlayer(self, dict):
        team = self.db.teams.find_one({'_id': ObjectId(dict['team'])})
        country = self.db.countries.find_one({'_id': ObjectId(dict['country'])})
        positions = [];
        for position in dict.getlist('positions'):
            newPosition = self.db.positions.find_one({'_id': ObjectId(position)})
            positions.append(newPosition)
        player = {'name': dict['name'], 'number': dict['number'], 'position': positions,
                 'team': team, 'country': country, 'price': int(dict['price'])}
        self.db.players.update_one({'_id': ObjectId(dict['edited_player'])}, {'$set': player })

    def sumByCountry(self):
        map = Code("""function(){
                              emit(this.country.name, this.price);
        		           };
        		           """)

        reduce = Code("""
        					  function(key, valuesPrices){
        						var sum = 0;
        						for (var i = 0; i < valuesPrices.length; i++) {
        						  sum += valuesPrices[i];
        						}
        						return sum;
        		              };
        		              """)
        results = self.db.players.map_reduce(map, reduce, "sum_by_country")
        return results.find()


    def sumByTeam(self):
        map = Code("""function(){
                              emit(this.team.full_name, this.price);
        		           };
        		           """)

        reduce = Code("""
        					  function(key, valuesPrices){
        						var sum = 0;
        						for (var i = 0; i < valuesPrices.length; i++) {
        						  sum += valuesPrices[i];
        						}
        						return sum;
        		              };
        		              """)
        results = self.db.players.map_reduce(map, reduce, "sum_by_team")
        return results.find()

    def countOfByPlayersByPositions(self):
        pipeline = [
            {"$unwind": "$position"},
            {"$group": {"_id": "$position.name", "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1)])}
        ]
        return list(self.db.players.aggregate(pipeline))

    def fill(self):
        count = len(teams)
        for i in range (1, 45000):
            name = teams[randint(0, count - 1)] + " - " + str(randint(0, 9))
            year = randint(1900, 2016)
            team = {'full_name': name, 'found_year': year}
            self.db.teams.insert(team)










