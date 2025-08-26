import requests
import json
import time
import sys
import util

payload = {
    "aid": 1988,
    "count": 5,
    # Seems to not matter? Just needs to exist.
    "msToken": "I23Ow6YAElpDSQDueUW63FKaiMlOyA-zi9UXKzMqgKfb5Db0c7Axd5yH___HYYbgBJIcVpb-E-smBC6zfw6RpFwM7AEMhLoyTeArT5k2KlNdRU4iXK0h_P3aTvU5zEGeWQYLa3OteBioeLz0Uij_Hw==",
    "cursor": 0,
    "secUid": None,  # defined in rssr.conf
}

def required_config_keys():
    return ['secUid']

def download_user_json(msToken, secUid):
    payload["msToken"] = msToken
    payload["secUid"] = secUid
    req = requests.get("https://www.tiktok.com/api/post/item_list/", params=payload)

    if req.status_code != 200:
        print(f"Failed with an error code of {req.status_code} -> {req.url}", file=sys.stderr)
        return None

    return json.loads(req.text) 

def parse_json(json):
    title = "<undefined>"
    link = "<undefined>"
    description = "<undefined>"

    items = []
    for video in json["itemList"]:
        tiktok_channel = video["author"]["uniqueId"]
        video_id = video["id"]
        video_link = f"https://www.tiktok.com/@{tiktok_channel}/video/{video_id}"

        items.append({
            "title": video["desc"],
            "link": video_link,
            "pubDate": util.rss_date_format(video["createTime"]),
            "guid": video_link,
            "description": ""
        })

    return ({
        "title": title,
        "link": link,
        "description": description,
        "generator": "rssr",
        "language": "en-gb",
        "lastBuildDate": util.rss_date_format(time.time()),
        "items": items
    })

def retrieve(config):
    if "TikTok" not in config:
        print(f"Required section [TikTok] needed in config (default ./rssr.conf)")
        for key in required_config_keys():
            print(f"Required key [TikTok] -> {key} not set in config (default ./rssr.conf).", file=sys.stderr)
        return None

    keyerror = False
    for key in required_config_keys():
        if key not in config["TikTok"].keys():
            print(f"Required key [TikTok] -> {key} not set in config (default ./rssr.conf).", file=sys.stderr)
            keyerror = True

    if keyerror:
        return None

    msToken = payload["msToken"]
    secUid = config["TikTok"].get("secUid")

    data = download_user_json(msToken, secUid)

    if data is None:
        return None
    
    return parse_json(data)
