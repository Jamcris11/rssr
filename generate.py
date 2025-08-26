from xml.etree.ElementTree import Element, SubElement, tostring
import time
import util

def generate_rss_xml(data, config):
    title = config['rss']['title'] if 'title' in config['rss'] else '<undefined>'
    link = config['rss']['link'] if 'link' in config['rss'] else '<undefined>'
    description = config['rss']['description'] if 'description' in config['rss'] else '<undefined>'
    lang = "en-gb" #config['rss']['lang']

    root = Element("rss", attrib={"version": "2.0"})
    channel = SubElement(root, "channel")
    SubElement(channel, "title").text = title if title else data["title"]
    SubElement(channel, "link").text = link if link else data["link"]
    SubElement(channel, "description").text = description if description else data["description"]
    SubElement(channel, "generator").text = "rssr"
    SubElement(channel, "language").text = lang if lang else "en-gb"
    SubElement(channel, "lastBuildDate").text = (
        util.rss_date_format(time.time())
    )

    for video in data["items"]:
        item = Element("item")
        SubElement(item, "title").text = video["title"]
        SubElement(item, "link").text = video["link"]
        SubElement(item, "pubDate").text = video["pubDate"]
        SubElement(item, "guid").text = video["guid"]
        channel.append(item)

    return tostring(root, encoding="unicode")
