CREATE TABLE rss (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR (50) NOT NULL UNIQUE,
    rss TEXT NOT NULL,
    channel VARCHAR (20) NOT NULL,
    favicon TEXT,
    freq INT,
    lastcheck DATETIME
);

CREATE TABLE webhook (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    url TEXT NOT NULL
);

INSERT INTO rss (name, rss, channel, favicon, freq, lastcheck) VALUES ("samplerss", "https://www.feedforall.com/sample.xml", "channel_name", "https://www.feedforall.com/favicon.ico", 432000, "2021-09-30 00:00:00");

INSERT INTO webhook(name, url) VALUES("channel_name", "YOUR_DISCORD_WEBHOOK_URL");
