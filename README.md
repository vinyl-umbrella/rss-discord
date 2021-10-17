# rss-discord
This programs send rss notif via discord webhook

### DB
- rss table
    - name = feed name
    - rss = feed url
    - channel = discord channel name
    - favicon = favicon url
    - freq = check frequency
    - lastcheck = last chack date

- webhook table
    - name = discord channel name
    - url = discord webhook ur

### how to use
1. set rss and webhook at ./db/data.sql
2. exec `docker-compose up`
3. abcd

### env
- python 3.8.10
- mariadb 15.1
