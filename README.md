# Music Library

-----

### Start Project

pyenv
````
python -m venv .venv
source .venv/bin/activate
````

Instalar dependencias
```
pip install -r requirements.txt
```

Iniciar container do Redir via docker compose
```shell script
docker-compose up -d
```

Variaveis de ambientes necessarias

#### AWS
```shell script
AWS_SECRET_ACCESS_KEY
AWS_ACCESS_KEY_ID
```

### GENIUS
```shell script
GENIUS_OUTH2
```

### Redis
```shell script
CACHE_REDIS_PASSWORD #default music-library!
CACHE_REDIS_PORT #default 6379
```

### Endpoint
####Get 
.../artists/16775/songs

Body Response
```json
{
    "artistName": "Sia",
    "songs": [
        {
            "fullTitle": "Dusk Till Dawn by ZAYN (Ft. Sia)",
            "id": 3219791,
            "primaryArtist": {
                "id": 339472,
                "name": "ZAYN",
                "url": "https://genius.com/artists/Zayn"
            },
            "title": "Dusk Till Dawn"
        }
}
```