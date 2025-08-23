#!/usr/bin/env python
# Copyright (c) 2025 Jim
# /

from bs4 import BeautifulSoup
from xml.etree.ElementTree import Element, SubElement, tostring
import datetime
import requests
import json

def download_itemlist_json(url):
    req = requests.get(url, auth=('user', 'pass'))

    if req.status_code != 200:
        print(f"Failed with an error of {req.status_code} -> {url}")
        return None

    return json.loads(req.text) 

with open("page.json", "r") as f:
    _json = json.load(f)

root = Element('rss')
channel = SubElement(root, "channel")
link = SubElement(channel, "link")
desc = SubElement(channel, "desc")
generator = SubElement(channel, "generator").text = "rssr"
language = SubElement(channel, "language").text = "en-gb"
lastBuildDate = SubElement(channel, "lastBuildDate").text = (
    datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0100")
)


for video in _json["itemList"]:
    tiktok_channel = video["author"]["uniqueId"]
    video_id = video["id"]
    link = f"https://www.tiktok.com/@{tiktok_channel}/video/{video_id}"

    item = SubElement(channel, "item")
    SubElement(item, "title").text = video["desc"]
    SubElement(item, "link").text = link 
    SubElement(item, "pubDate").text = datetime.datetime.fromtimestamp(video["createTime"]).strftime("%a, %d %b %Y %H:%M:%S +0100")
    SubElement(item, "guid").text = link

#[ SubElement(SubElement(channel, "item"), "title") for x in _json["itemList"] for y in x["contents"] ]

print(tostring(root, encoding="unicode"))

