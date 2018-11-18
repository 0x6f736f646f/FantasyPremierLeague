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
	



def main():
	parse_data()

if __name__ == '__main__':
	main()