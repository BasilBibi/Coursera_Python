import json
import urllib.request, urllib.parse, urllib.error


def crawl_comments_json(url_lib, url):
    js = url_lib.request.urlopen(url).read()
    json_dict = json.loads(js)
    comments = json_dict['comments']
    counts = [ int( i['count'] ) for i in comments]
    return sum(counts)
