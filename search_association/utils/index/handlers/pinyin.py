# @Author: weirdgiser
# @Time: 2024/1/23
# @Function:
# Dependency:
#  - pypinyin https://github.com/mozillazg/python-pinyin#id1
# lazy_pinyin return pinyin without 声调
from pypinyin import pinyin, lazy_pinyin, Style
from utils.index.handlers.base import BaseIndexHandler


def get_first_pinyin_letter(word):
    res = pinyin(word, style=Style.FIRST_LETTER, heteronym=False)
    return [r[0] for r in res]


def get_pinyin(word):
    return lazy_pinyin(word)


class PinyinIndexHandler(BaseIndexHandler):
    def get_pinyin_full_index(self, word):
        pinyin_full = get_pinyin(word)
        return "".join(pinyin_full)

    def get_pinyin_first_letter(self, word):
        pinyin_first_letter = get_first_pinyin_letter(word)
        return "".join(pinyin_first_letter)

    def process_document(self, document):
        return [self.get_pinyin_full_index(document), self.get_pinyin_first_letter(document)]
