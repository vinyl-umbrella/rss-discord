from datetime import datetime
import feedparser
import time

import db
from discord_data import discord_data


def make_datetime(parsed_date):
    dt = datetime(parsed_date.tm_year, parsed_date.tm_mon, parsed_date.tm_mday,
                  parsed_date.tm_hour, parsed_date.tm_min, parsed_date.tm_sec)
    return dt


conf = db.get_config()
now = datetime.utcnow()
for site in conf:
    td = now - site["lastcheck"]
    # print(site["name"], td)

    # 現在時刻とlastcheckを比較し，freqより大きい時のみ実行
    if td.total_seconds() > site["freq"]:
        r = feedparser.parse(site["rss"])

        if r.status == 200:
            for item in reversed(r.entries):
                try:
                    updated_at = make_datetime(item.published_parsed)
                except AttributeError:
                    updated_at = make_datetime(item.updated_parsed)

                # 新着のみpost
                # print(site["lastcheck"], updated_at, now.strftime("%Y-%m-%d %H:%M:%S"))
                if site["lastcheck"] < updated_at:
                    data = discord_data(site["name"], site["favicon"], item.link, site["url"])
                    res = data.post_to_discord()
                    time.sleep(0.3)
                    if not res[0]:
                        print(res[1])

        db.update_lastcheck(now.strftime("%Y-%m-%d %H:%M:%S"), site["name"])
        time.sleep(1)
