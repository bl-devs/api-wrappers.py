# botlista-wrapper
## dokumentacja

#### Instalacja biblioteki
Bibliotekę instalujemy poprzez polecenie ```pip install git+https://github.com/ivall/botlista-wrapper#egg=botlistawrapper```

### Importowanie
```python
from botlistawrapper.main import BotLista
```

# Użycie
```python
client = BotLista(bot_id)
bot = BotLista.get_bot()
```
Teraz mamy dostęp do klasy Bot (patrz models/bot.py) i jej metod. Na przykład id bota uzyskamy w następujący sposób:
```python
bot_id = bot.botID
```
