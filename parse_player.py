import csv
import os

def extract_stat_names(dictionary_of_stats):
	statistic_topic_name = []
	for key, val in dictionary_of_stats.items():
		statistic_topic_name += [key]
	return statistic_topic_name

def parse_players(list_of_players, base_filename):
	#We are extraxting topic names for statistics
	statistic_topic_name = extract_stat_names(list_of_players[0])
	filename = base_filename + "players_initial.csv"
	os.makedirs(os.path.dirname(filename))
	file_open = open(filename, "w+", encoding="utf8", newline="")
	file_write = csv.DictWriter(file_open, statistic_topic_name)
	file_write.writeheader()
	for player in list_of_players:
		file_write.writerow({key:str(val).encode("utf-8").decode("utf-8") for key, val in player.items()})

