import os

# mysql config
RELATION_DB_PWD = os.getenv("RELATION_DB_PWD", "Turing@123")
RELATION_DB_USER = os.getenv("RELATION_DB_USER", "root")
RELATION_DB_HOST = os.getenv("RELATION_DB_HOST", "192.168.31.160")
RELATION_DB_PORT = os.getenv("RELATION_DB_PORT", "3306")
RELATION_DB_NAME = os.getenv("RELATION_DB_NAME", "media_crawler")

RELATION_DB_URL = f"mysql://{RELATION_DB_USER}:{RELATION_DB_PWD}@{RELATION_DB_HOST}:{RELATION_DB_PORT}/{RELATION_DB_NAME}"

# redis config
REDIS_DB_HOST = "192.168.31.119"  # your redis host
REDIS_DB_PWD = os.getenv("REDIS_DB_PWD", "Turing@123")  # your redis password
REDIS_DB_PORT = os.getenv("REDIS_DB_PORT", 6379)  # your redis port
REDIS_DB_NUM = os.getenv("REDIS_DB_NUM", 0)  # your redis db num

# cache type
CACHE_TYPE_REDIS = "redis"
CACHE_TYPE_MEMORY = "memory"