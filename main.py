#!/usr/bin/env ./pvenv/bin/python
# Copyright (c) 2025 Jim
# /

from TikTokApi import TikTokApi
import asyncio
import os
from xml.etree.ElementTree import Element, SubElement, tostring
import datetime
import requests
import json

appid = 1988
count = 35
ms_token = "iVzn4V-A4bPy3NNJAxLcrBUtEsVOk6qom3pffTEOQ7odCtLvlbqaETWcZ8Ih91FJLHXHIngv_uEcp9nlC3rdT8GwgEfHfnWHeoM9hRcJdqBlRNTCYK4zwr1uHiYeWEFkcznKZk9_3eZRkHYUenM1"
sec_uid = "MS4wLjABAAAAzXa4i_wZ8O3DdHEsw-sKLizL7VlFfiNvZ9IHI5_U94CB6JNedAdyJWKEd2bmODPM"

payload = {
    "aid": appid,
    "count": count,
    "msToken": ms_token,
    "cursor": 0,
    "secUid": sec_uid,
}

def download_itemlist_json():
    req = requests.get("https://www.tiktok.com/api/post/item_list/", params=payload)

    if req.status_code != 200:
        print(f"Failed with an error of {req.status_code} -> {url}")
        return None

    return json.loads(req.text) 

#with open("page.json", "r") as f:
#    _json = json.load(f)

_json = download_itemlist_json()

root = Element("rss", attrib={"version": "2.0"})
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

