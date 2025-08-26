import datetime

def rss_date_format(timestamp):
    return (
        datetime.datetime
            .fromtimestamp(timestamp)
            .strftime("%a, %d %b %Y %H:%M:%S +0100")
    )


