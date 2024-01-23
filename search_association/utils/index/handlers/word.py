# @Author: weirdgiser
# @Time: 2024/1/23
# @Function:
from utils.index.handlers.base import BaseIndexHandler
import jieba
class WordSegIndexHandler(BaseIndexHandler):
    """
    分词、大小写
    """
    def process_document(self, document):
        if isinstance(document, str):
            seg_list = jieba.cut_for_search(document)
            return seg_list
        else:
            raise ValueError(document)

class WordLetterIndexHandler(BaseIndexHandler):
    """
    分词、大小写
    """
    def process_document(self, document):
        if isinstance(document, str):
            return (document.lower(), document.upper())
        else:
            raise ValueError()