import unittest
import time
from utils.index.handlers.word import WordSegIndexHandler, WordLetterIndexHandler
from utils.index.handlers.pinyin import PinyinIndexHandler, get_pinyin, get_first_pinyin_letter
from utils.index.persist import SimpleMemoryIndexPersist
from utils.index.indexers import IndexerProxy
class IndexTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.word_handler = WordSegIndexHandler()

    def test_word_seg_handler(self):
        cases = ["AI算法", "机器学习", "OpenAI", "openai", "AI框架", "项目投资事件", "数据库安全","小明硕士毕业于中国科学院计算所，后在日本京都大学深造"]
        for case in  cases:
            seg_list = self.word_handler.process_document(case)
            print(f"{case}: {','.join(seg_list)}")

    def test_pinyin_handler(self):
        pinyin_handler = PinyinIndexHandler()
        cases = ["AI算法", "机器学习", "OpenAI", "openai", "AI框架", "项目投资事件", "数据库安全","小明硕士毕业于中国科学院计算所，后在日本京都大学深造"]
        for case in  cases:
            seg_list = pinyin_handler.process_document(case)
            print(f"{case}: {','.join(seg_list)}")
            # print(f"{case}:", get_pinyin(case), get_first_pinyin_letter(case))
    def test_word_handlers(self):
        handlers = (WordLetterIndexHandler(),)
        for handler in handlers:
            res = handler.process_document("OpenAI")
            print(res)

    def test_indexer(self):
        indexer = IndexerProxy()
        word_letter_handler = WordLetterIndexHandler()
        word_seg_handler = WordSegIndexHandler()
        indexer.add_handler(word_seg_handler, word_letter_handler)
        cases = ["学习","AI算法", "机器学习", "我是一个投篮高手","<机器学习>", "《机器学习》","天天学习》好好像上","OpenAI", "openai", "AI框架", "投融资事件","项目投资事件", "数据库安全","小明硕士毕业于中国科学院计算所，后在日本京都大学深造"]
        for case in cases:
            indexer.process(case)
        indexer.persist.index_construction_trigger()
        print("====test index====")
        words_to_test = ("AI", "学习", "框架", "投资", "数据", "机器", "open", "OpEn", "OpenaI")
        for word in words_to_test:
            start_time = time.time()
            res = indexer.search_index(word)
            print(f"{word}: {res}")
            end_time = time.time()
            print("time cost: ", end_time-start_time)
        print("====test prefix====")
        words_to_test = ("投篮","学习","AI", "学", "框架", "投", "数据", "机器", "open", "机", "OpenaI", "A", "a", "OpEn")
        for word in words_to_test:
            start_time = time.time()
            res = indexer.search_word_with_suggest(word)
            end_time = time.time()
            print(f"{word}: {res}")
            print("time cost: ", end_time - start_time)


if __name__ == '__main__':
    unittest.main()
