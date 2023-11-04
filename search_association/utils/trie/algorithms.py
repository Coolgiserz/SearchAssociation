"""
给定数据列表，返回Trie树用于检索
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_association.settings')
from django.conf import settings

django.setup()
from game.models import TGame
from utils.trie.struct_ import TrieTree

class SearchAssociation:
    def __init__(self):
        tree = TrieTree()

    def run(self):
        return TGame.objects.values("name_zh").all()