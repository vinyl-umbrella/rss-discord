from dataclasses import dataclass, asdict
import requests


@dataclass
class discord_data:
    username: str = "rss"
    avatar_url: str = "https://cdn-icons-png.flaticon.com/512/179/179336.png"
    content: str = ""
    webhook: str = ""

    def post_to_discord(self):
        res = requests.post(self.webhook, data=asdict(self))
        return [res.ok, res.text]
