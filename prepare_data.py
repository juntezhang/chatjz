import json

f = open('./data/brunnen.json')

data = json.load(f)

for v in data['features']:
    coordinates = v['geometry']['coordinates']
    type = v['properties']['brunnenart_txt']
    poi = v['properties']['bezeichnung'] if v['properties']['bezeichnung'] is not None else ''
    print('{"prompt":"'+type+' (fountain in Zurich) ->","completion":" '+str(coordinates)+' '+poi+'###"}')

f.close()
