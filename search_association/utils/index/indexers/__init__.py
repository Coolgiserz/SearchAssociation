# @Author: weirdgiser
# @Time: 2024/1/23
# @Function:
import asyncio
from utils.index.handlers import WordSegIndexHandler, WordLetterIndexHandler, PinyinIndexHandler
from utils.index.persist import SimpleMemoryIndexPersist, IndexPersist
import tqdm

class IndexerProxy(object):
    def __init__(self, persist_class=None):
        self.handlers = []
        if persist_class is None:
            self.persist = SimpleMemoryIndexPersist()
        else:
            assert isinstance(persist_class, IndexPersist)
            self.persist = persist_class

    def add_handler(self, *handler):
        self.handlers.extend(handler)

    def process(self, document):
        for handler in self.handlers:
            assert hasattr(handler, "process_document")
            indexs = handler.process_document(document)
            for index in indexs:
                self.persist.add_one(index, document)

    def process_documents(self, documents):
        for document in tqdm.tqdm(documents):
            self.process(document)

    def get_all_indexes(self):
        return self.persist.get_indexes

    def search_index(self, index: str):
        return self.persist.search(index.lower())

    def search_word_with_suggest(self, word: str):
        return self.persist.search_prefix(word)


class SimpleIndexProxy(IndexerProxy):
    def __init__(self, persist_class):
        super().__init__(persist_class)
        self.handlers = [WordLetterIndexHandler(),
                         WordSegIndexHandler(),
                         PinyinIndexHandler()]

    @classmethod
    def init_index_proxy_from_words(cls, words, persist_class=None, from_scratch=True):
        print(f"init index proxy from {len(words)} words")
        sip = SimpleIndexProxy(persist_class)
        if from_scratch:
            sip.process_documents(documents=words)
        else:
            print("索引已存在")
        sip.persist.index_construction_trigger()
        return sip
