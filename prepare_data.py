import json
import os

RUN = os.getenv('RUN', 0)

file = "./data/brunnen.json"
if RUN != 0:
    file = './data/wvz.wvz_brunnen.json'

f = open(file)
data = json.load(f)

for v in data['features']:
    coordinates = v['geometry']['coordinates']

    if RUN != 0:
        type = v['properties']['art']
        quartier = v['properties']['quartier'] if v['properties']['quartier'] else 'unknown district'
        place_name = v['properties']['ortsbezeichnung'] if v['properties']['ortsbezeichnung'] else 'unknown name'
        print('{"prompt":"'+type+' (fountain in Zurich) ->","completion":" '+place_name+' '+str(coordinates)+' '+quartier+'###"}')
    else:
        type = v['properties']['brunnenart_txt']
        poi = v['properties']['bezeichnung'] if v['properties']['bezeichnung'] is not None else ''
        print('{"prompt":"' + type + ' (fountain in Zurich) ->","completion":" ' + str(coordinates) + ' ' + poi + '###"}')

f.close()
