#!/usr/bin/python3
"""
===============================
Scripti ya kuongeza hoja za amri kwenye orodha na kuziokoa kwenye faili ya JSON
===============================
"""

import sys
import os

# Kuingiza kazi kwa njia ya __import__()
hifadhi_kwenye_faili = __import__('5-save_to_json_file').save_to_json_file
pata_kutoka_kwa_faili = __import__('6-load_from_json_file').load_from_json_file

faili = "add_item.json"

# Kuanza orodha
if os.path.exists(faili):
    orodha_yangu = pata_kutoka_kwa_faili(faili)
else:
    orodha_yangu = []

# Ongeza hoja zote za amri kwenye orodha (bila jina la script)
orodha_yangu.extend(sys.argv[1:])

# Hifadhi orodha iliyo sasishwa kwenye faili ya JSON
hifadhi_kwenye_faili(orodha_yangu, faili)
