import unittest
from utils.index.persist.db import RedisIndexPersist

class RedisIndexPersistTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.redis_persist = RedisIndexPersist()
        self.redis_persist.init_connection()

    def test_check_connection(self):

        self.redis_persist.check_connection()

    def test_flush_db(self):
        self.redis_persist.redis_handler.flushdb()

    def test_add_and_search(self):
        self.redis_persist.add_one("机器", "机器学习")
        self.redis_persist.add_one("机器", "机器跳舞")
        self.redis_persist.add_one("机器", "无限机器学习")
        self.redis_persist.add_one("机器", "无限机器学习")

        self.redis_persist.add_one("机机复唧唧", "木兰辞机机复唧唧")
        print(self.redis_persist.search("机"))
        print(self.redis_persist.search("机器"))

    def test_get_indexes(self):
        print(self.redis_persist.get_indexes())

    def test_search_prefix(self):
        print(self.redis_persist.search_prefix("机"))
        print(self.redis_persist.search_prefix("机器"))

if __name__ == '__main__':
    unittest.main()
