from urllib import request, error, parse
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + parse.urlencode({
        "address": address,
        "key": "Needs billing api key"
    })

    print('Retriving', url)
    uh = request.urlopen(url)
    data = uh.read().decode()
    print('Retrived', len(data), 'characters')

    try: 
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure:', data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted address']
    print(location)