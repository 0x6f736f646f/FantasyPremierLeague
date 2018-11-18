import requests
import json
import time

def get_data():
    response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static")
    if response.status_code != 200:
        raise Exception("Response code was: {}".format(response.status_code))
    else:
        response_text = response.text
        data = json.loads(response_text)
        #print("Data was collected")
        #This is for debugging purposes
        return data

def get_individual_player_data(player_id):
    base_url = "https://fantasy.premierleague.com/drf/element-summary/"
    full_url = base_url + str(player_id)
    response = requests.get(full_url)
    if response.status_code != 200:
        raise Exception("Response code was: {}".format(response.status_code))
    else:
        response_text = response.text
        data = json.loads(response_text)
        return data