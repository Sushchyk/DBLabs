from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.code import Code
from bson.son import SON

class DatabaseManager:

    def __init__(self):
            self.client = MongoClient()
            self.db = self.client.lab2

    def fillDb(self):
            self.db.insert('')

    def getAllTeams(self):
        teams = [team for team in self.db.teams.find()] # Return list of teams
        for team in teams:
            team['found_year'] = int(team['found_year'])
        return teams

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
                 'team': team, 'country': country, 'price': dict['price']}
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
                 'team': team, 'country': country, 'price': dict['price']}
        self.db.players.update_one({'_id': ObjectId(dict['edited_player'])}, {'$set': player })





