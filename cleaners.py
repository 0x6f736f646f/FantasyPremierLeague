import csv
import math
import os

def clean_players(filename, base_filename):
	headers = ['first_name','second_name', 'now_cost', 'value_form', 'value_season', 'selected_by_percent', 'form', 'total_points', 'event_points', 'points_per_game', 'minutes', 'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat', 'ict_index',]
	fopen = open(filename, "r+", encoding="utf-8")
	outname = base_filename + "cleaned_players.csv"
	#os.makedirs(os.path.dirname(outname))
	fout = open(outname, "w+", encoding="utf-8", newline="")
	reader = csv.DictReader(fopen)
	writer = csv.DictWriter(fout, headers, extrasaction="ignore")
	writer.writeheader()
	for line in reader:
		writer.writerow(line)

def ids_of_players(player_filename, base_filename):
	headers = ['first_name','second_name', 'id']
	fopen = open(player_filename, "r+", encoding="utf-8")
	outname = base_filename + "player_ids_list.csv"
	fout = open(outname, "w+", encoding="utf-8", newline="")
	reader = csv.DictReader(fopen)
	writer = csv.DictWriter(fout, headers, extrasaction="ignore")
	writer.writeheader()
	for line in reader:
		writer.writerow(line)