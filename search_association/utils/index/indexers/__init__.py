# @Author: weirdgiser
# @Time: 2024/1/23
# @Function:
import asyncio
from utils.index.handlers.base import BaseIndexHandler
from utils.index.persist import SimpleMemoryIndexPersist, IndexPersist
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
            # assert isinstance(handler, BaseIndexHandler)
            indexs = handler.process_document(document)
            for index in indexs:
                self.persist.add_one(index, document)

    def search_index(self, index:str):
        return self.persist.search(index.lower())

    def search_word_with_suggest(self, word: str):
        return self.persist.search_prefix(word)
