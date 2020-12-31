import requests

from models.bot import Bot
from exceptions import BotNotFound, InternalServerError


class BotLista:
    def __init__(self, bot_id: int):
        self.bot_id = bot_id

    def get_bot(self) -> Bot:
        r = requests.get(f'https://botlista.pl/api/bots/{self.bot_id}').json()

        if 'status' in r:
            message = r['message']

            if r['status'] == 404:
                raise BotNotFound(message)
            elif r['status'] == 500:
                raise InternalServerError(message)

        return Bot(r)

