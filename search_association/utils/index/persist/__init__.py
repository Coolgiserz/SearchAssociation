# @Author: weirdgiser
# @Time: 2024/1/23
# @Function: Base Class For Index Persist

from collections import defaultdict,Counter
from utils.trie.struct_ import TrieTree
class IndexPersist(object):
    def add_one(self, index, document):
        pass

    def add_multi(self, index_documents):
        pass

    def search(self, index):
        pass

    def get_indexes(self):
        pass

    def search_prefix(self, word):
        pass
    def index_construction_trigger(self):
        pass

class SimpleMemoryIndexPersist(IndexPersist):
    def __init__(self):
        self.index_map = defaultdict(Counter)
        self.trie = TrieTree()

    @property
    def get_indexes(self):
        return self.index_map.keys()
    def add_one(self, index, document):
        self.index_map[index][document] += 1

    def search(self, index, desc=True):
        counter =  self.index_map[index]

        sorted_keys = [key for key, _ in counter.most_common()]
        if not desc:
            sorted_keys = sorted_keys[::-1]
        return sorted_keys

    def build_trie(self):
        for index, _ in self.index_map.items():
            # for document, _ in counter.items():
                self.trie.insert(index.lower())

    def index_construction_trigger(self):
        self.build_trie()

    def search_prefix(self, word):
        indexs = self.trie.startwith(word.lower())
        result = list()
        for index in indexs:
            res = self.search(index)
            result.extend(res)
        return list(set(result))

