import json


def fetch_place_id(urllib, url, address):

    full_url = url + urllib.parse.urlencode({'address': address})
    d = urllib.request.urlopen(full_url).read()
    data = d.decode()

    js = json.loads(data)

    print(json.dumps(js, indent=2)[0:200]+'...')

    place_id = js["results"][0]["place_id"]

    return place_id
