import os
import pymysql.cursors


def connect_db():
    conn = pymysql.connect(host='192.168.200.12',
                           user=os.environ['MYSQL_USER'],
                           password=os.environ['MYSQL_PASSWORD'],
                           database=os.environ['MYSQL_DATABASE'],
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def get_config() -> list:
    with connect_db() as conn:
        with conn.cursor() as cur:
            sql = """
            SELECT rss.name, rss.rss, rss.favicon, rss.freq, rss.lastcheck, webhook.url
            FROM rss
            INNER JOIN webhook
            ON rss.channel = webhook.name;
            """
            cur.execute(sql)

            res = cur.fetchall()
        return res


def update_lastcheck(date, name):
    # 最終チェック日を更新
    with connect_db() as conn:
        with conn.cursor() as cur:
            sql = "UPDATE rss SET lastcheck = %s WHERE name = %s"
            cur.execute(sql, (date, name))
        conn.commit()


if __name__ == "__main__":
    print(get_config())
