# @Author: weirdgiser
# @Time: 2024/1/24
# @Function:
from utils.index.handlers.pinyin import PinyinIndexHandler
from utils.index.handlers.word import WordLetterIndexHandler, WordSegIndexHandler
__all__ = [
    WordLetterIndexHandler,
    WordSegIndexHandler,
    PinyinIndexHandler
]