import requests
import json
import socket

local_url = "http://127.0.0.1:5000"
# data
names = open("./hard_cards/names.txt", "r")
accords = open("./hard_cards/accords.txt", "r")
descs = open("./hard_cards/descs.txt", "r")
imgs_lnk = open("./hard_cards/imgs_lnk.txt", "r")
vids_lnk = open("./hard_cards/vids_lnk.txt", "r")
start_time = open("./hard_cards/start_times.txt", "r")

for i in range(12







json_headers = {'content-type': 'application/json'}






