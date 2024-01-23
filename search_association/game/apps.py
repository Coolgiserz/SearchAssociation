import os
import time
from django.apps import AppConfig
from django.conf import settings
from utils.trie.struct_ import TrieTree
from utils.index.handlers.word import WordSegIndexHandler, WordLetterIndexHandler
from utils.index.persist import SimpleMemoryIndexPersist
from utils.index.indexers import IndexerProxy
game_name_association_flag_string = "ASSOCIATION_FLAG_STRING"

class GameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game'

    def ready(self):
        """
        使用--noreload参数启动，可以
        :return:
        """
        # TODO： 初始化完之后对Trie树进行持久化存储
        print("初始化Game联想算法...")

        if os.environ.get("RUN_MAIN"):
            # 无需使用noreload标志启动server即可避免ready方法执行两次
            print("game app ready")
            flag = False
            try:
                flag = getattr(settings, game_name_association_flag_string, False)
            except:
                # 如果未设置,则设置为False
                setattr(settings, game_name_association_flag_string, False)
            finally:
                if not flag:
                    # https://docs.djangoproject.com/zh-hans/4.2/ref/applications/
                    TGame = self.get_model("TGame")
                    self.game_names_obj = TGame.objects.values("name_zh").all()
                    self.init_trie_tree()
                    self.init_index_proxy()

    def init_trie_tree(self):
        tree = TrieTree()
        for name in self.game_names_obj:
            tree.insert(name.get("name_zh"))
        setattr(settings, "game_name_association_trie", tree)
        print("Game-Trie树初始化完成！")

    def init_index_proxy(self):
        """
        初始化倒排索引代理
        :return:
        """
        start_time = time.time()
        index_proxy = IndexerProxy()
        word_letter_handler = WordLetterIndexHandler()
        word_seg_handler = WordSegIndexHandler()
        index_proxy.add_handler(word_seg_handler, word_letter_handler)
        for name in self.game_names_obj:
            index_proxy.process(name.get("name_zh"))
        index_proxy.persist.index_construction_trigger()
        setattr(settings, "game_name_association_index_proxy", index_proxy)
        end_time = time.time()
        print("time cost: ", end_time - start_time)
        print(f"Game-倒排索引初始化完成！Cost: {end_time - start_time}")






