# @Author: weirdgiser
# @Time: 2024/1/25
# @Function:
import os
from pathlib import Path
from configparser import ConfigParser
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
CONFIG_DIR = os.path.join(BASE_DIR, "config")

CACHE_SECTION = "cache"
config_parser = ConfigParser()
if DEBUG is True:
    CONFIG_PATH = os.path.join(CONFIG_DIR, "dev.conf")
else:
    CONFIG_PATH = os.path.join(CONFIG_DIR, "pro.conf")

config_parser.read(CONFIG_PATH)

# Redis配置
REDIS_HOST = config_parser.get(CACHE_SECTION, "REDIS_HOST")
REDIS_PORT = config_parser.get(CACHE_SECTION, "REDIS_PORT")
REDIS_DBNAME = config_parser.get(CACHE_SECTION, "REDIS_DBNAME")