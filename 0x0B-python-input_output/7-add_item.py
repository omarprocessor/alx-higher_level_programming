#!/usr/bin/python3
"""Moduli ya kuhifadhi kwenye JSON."""
import json
import os.path
import sys
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = []

# Angalia kama faili lipo
if os.path.exists(filename):
    try:
        json_list = load_from_json_file(filename)
    except json.decoder.JSONDecodeError:
        json_list = []  # Tathmini orodha kama faili ni tupsahihi

# Ongeza hoja zote za amri kwenye orodha
for index in argv[1:]:
    json_list.append(index)

# Hifadhi orodha kwenye faili la JSON
save_to_json_file(json_list, filename)
