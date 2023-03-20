import json

f = open('./data/brunnen.json')

data = json.load(f)

for v in data['features']:
    coordinates = v['geometry']['coordinates']
    type = v['properties']['brunnenart_txt']
    print('{"prompt":"'+type+' (fountain in Zurich) ->","completion":" '+str(coordinates)+'###"}')

f.close()
