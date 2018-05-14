import json
import urllib.request, urllib.parse, urllib.error


def fetch_place_id(url, address):
    full_url = url + urllib.parse.urlencode( {'address': address} )

    data = urllib.request.urlopen(full_url).read().decode()

    js = json.loads(data)

    print(json.dumps(js, indent=2))

    place_id = js["results"][0]["place_id"]

    return place_id
