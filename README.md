**Really Simple Syndication Replicator** (**rssr**) pronounced 
['**aire es es aire**'] is an rss feed generator for content not officially 
supporting rss.

The program source can be found on [GitHub](https://github.com/Jamcris11/rssr).

#### Currently supported
- TikTok user video uploads
## Usage

```sh
usage: rssr [-h] [-c config] [-e] [-t title] [-l link] [-d description] outputfile

positional arguments:
  outputfile

options:
  -h, --help      show this help message and exit
  -e              checks outputfile exists and only overwrites with new entries
  -c config       path to config file (default is ./rssr.conf)
  -t title        set title for rss feed, overrides config
  -l link         sets link for rss feed, overrides config
  -d description  sets description for rss feed, overrides config
```

### Example 
```sh
rssr -e -c tiktok_<username>.conf tiktok_<username>.xml
```

#### tiktok\_\<username\>.conf
```INI
[rss]
title 		= TikTok feed of @<username>
link  		= https://jimscorner.co.uk/feeds/tiktok_<username>.xml
description = An rssr generated rss feed for the TikTok user @<username>

[TikTok]
secUid = MS4wLjABAAAAzXa4i_wZ8O3DdHEsw-sKLizL7VlFfiNvZ9IHI5_U94CB6JNedAdyJWKEd2bmODPM
```

**secUid** is REQUIRED for a TikTok user, and it is unique to every user, the way 
to obtain it is to look at a TikTok user's GET '**api/post/item\_list**' request, 
and grabbing it from the GET parameters. 
(Currently looking at for a less involved method of obtaining this.)

## Background
I started watching @officialvarg TikTok videos and wanted to be notified when he 
uploaded new content, not having a TikTok account and not wanting to create on
I decided I wanted a way to integrate notifications into my already existing 
rss, but TikTok provides no official rss feed support from their website. 
So I started making this program to utilise TikTok's POST request's to get the 
relevant data and compile it into a usable rss.xml, which I then can self-host 
for my rss-clients to connect to (see [feeds.](https://jimscorner.co.uk/feeds/))

Whilst TikTok user videos are currently the only supported unofficial content
and main motivation for making **rssr**, I've left it open for implementations 
of other types of content.

You can read about [how I use rssr here](https://jimscorner.co.uk/posts/rssr-personal-setup/).
