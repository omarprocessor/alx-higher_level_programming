#!/usr/bin/python3
"""
===============================
Scripti inayoongeza hoja za amri kwenye orodha na kuziokoa kwenye faili ya JSON
===============================
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Kuanza orodha
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Ongeza hoja zote za amri kwenye orodha (bila jina la script)
my_list.extend(sys.argv[1:])

# Hifadhi orodha iliyo sasishwa kwenye faili ya JSON
save_to_json_file(my_list, filename)
