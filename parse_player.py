import csv
import os

def extract_names(stats):
	title_name = []
	for key, val in stats.items():
		title_name += [key]
	return title_name

def parse_players(list_of_players, base_filename):
	#We are extraxting topic names for statistics
	title_name = extract_names(list_of_players[0])
	filename = base_filename + "players_initial.csv"
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	file_open = open(filename, "w+", encoding="utf8", newline="")
	file_write = csv.DictWriter(file_open, title_name)
	file_write.writeheader()
	for player in list_of_players:
		file_write.writerow({key:str(val).encode("utf-8").decode("utf-8") for key, val in player.items()})

def parse_player_history(histories, base_filename, player_name, Id):
	if len(histories) > 0:
		title_names = extract_names(histories[0])
		filename = base_filename + player_name + '/history.csv'
		os.makedirs(os.path.dirname(filename), exist_ok=True)
		file_open = open(filename, "w+", encoding="utf-8" , newline="")
		file_write = csv.DictWriter(file_open, title_names)
		file_write.writeheader()
		for history in histories:
			file_write.writerow(history)

def parse_player_gw_history(gameweeks, base_filename, player_name, Id):
    if len(gameweeks) > 0:
        title_names = extract_names(gameweeks[0])
        filename = base_filename + player_name + '/gw.csv'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, 'w+', encoding='utf8', newline='')
        w = csv.DictWriter(f, title_names)
        w.writeheader()
        for gw in gameweeks:
            w.writerow(gw)
