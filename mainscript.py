from Data import *
import requests
import json
import time
from parse_player import *
from cleaners import *

def parse_data():
	print("Starting streaming for fpl api")
	all_data = get_data()
	season = "2018"
	base_filename = "Data/{}/".format(season)
	print("Getting summary data")
	parse_players(all_data["elements"], base_filename)
	print("Cleaning summary data")
	clean_players(base_filename + "players_initial.csv", base_filename)
	print("Getting individual player ids")
	ids_of_players(base_filename + "players_initial.csv", base_filename)
	player_ids = get_player_ids(base_filename)
	num_players = len(all_data["elements"])
	player_base_filename = base_filename + "players/"
	gameweek_base_filename = base_filename + "gameweeks/"
	print("Extracting specific player Data")
	for i in range(num_players):
		player_data = get_individual_player_data(i+1)
		parse_player_history(player_data["history_past"], player_base_filename, player_ids[i+1], i+1)
		parse_player_gw_history(player_data["history"], player_base_filename, player_ids[i+1], i+1)
		print("{} : Getting Data for player : {}".format(i+1, player_ids[i+1]))
		
def main():
	parse_data()

if __name__ == '__main__':
	main()