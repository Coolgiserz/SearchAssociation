import unittest
from utils.index.indexers import SimpleIndexProxy


class SimpleIndexTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_something(self):
        cases = ["AI算法", "机器学习", "OpenAI", "openai", "AI框架", "项目投资事件", "数据库安全","小明硕士毕业于中国科学院计算所，后在日本京都大学深造"]

        self.proxy = SimpleIndexProxy.init_index_proxy_from_words(cases)
        print("all index: ", self.proxy.get_all_indexes())

        querys = ["j", "J", "A", "ai", "jq", "机"]
        for query in querys:
            print(f"query {query} ", self.proxy.search_word_with_suggest(query))



if __name__ == '__main__':
    unittest.main()
