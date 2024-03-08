# @Author: weirdgiser
# @Time: 2024/1/25
# @Function:
import redis
from utils.index.persist import IndexPersist
from utils.trie.struct_ import TrieTree

from constant import config

class RedisIndexPersist(IndexPersist):
    def __init__(self):
        self.redis_handler = None
        self.trie = None
        self.init_connection()

    def build_trie(self):
        self.trie = TrieTree()
        for index in self.get_indexes:
            self.trie.insert(index.lower())


    def check_connection(self):
        if self.redis_handler is None:
            return False
        try:
            response = self.redis_handler.ping()
            if response:
                print("Redis 连接正常")
                return True
            else:
                print("Redis 连接异常")
                return False
        except redis.exceptions.ConnectionError as e:
            print("无法连接到 Redis:", str(e))
            return False

    def init_connection(self):
        self.redis_handler = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DBNAME)


    @property
    def get_indexes(self):
        keys = self.redis_handler.keys("*")
        return [m.decode() for m in keys]

    def add_one(self, index, document):
        self.redis_handler.sadd(index, document)

    def search(self, index):
        members = self.redis_handler.smembers(index)
        return [m.decode() for m in members]

    def search_prefix(self, word):
        if self.trie is None:
            self.build_trie()
        indexs = self.trie.startwith(word.lower())
        result = list()
        for index in indexs:
            res = self.search(index)
            result.extend(res)
        return result
