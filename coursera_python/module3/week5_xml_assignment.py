import xml.etree.ElementTree as ET
import urllib.request, urllib.error


def crawl_xml(url_lib, url):
    xml = url_lib.request.urlopen(url).read()
    xml_element_tree = ET.fromstring(xml)
    results = xml_element_tree.findall('comments/comment')
    count = 0
    for comment in results:
        cnt = comment.find("count").text
        count = count + int(cnt)
    return count
