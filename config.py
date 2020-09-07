import os


class Config:
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    CACHE_DEFAULT_TIMEOUT = os.environ.get('CACHE_DEFAULT_TIMEOUT', 86000)
    CACHE_REDIS_PASSWORD = os.environ.get('CACHE_REDIS_PASSWORD', 'music-library!')
    CACHE_REDIS_PORT = os.environ.get('CACHE_REDIS_PORT', 6379)