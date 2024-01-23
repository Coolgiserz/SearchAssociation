import os
import time
from django.apps import AppConfig
from django.conf import settings
from utils.trie.struct_ import TrieTree
from utils.index.handlers.word import WordSegIndexHandler, WordLetterIndexHandler
from utils.index.persist import SimpleMemoryIndexPersist
from utils.index.indexers import IndexerProxy

industry_name_association_flag_string = "industry_name_association_flag_string"
class IndustryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'industry'
    def ready(self):
        """
        使用--noreload参数启动，可以
        :return:
        """
        print("初始化联想算法-行业图谱...")
        if os.environ.get("RUN_MAIN"):
            # 无需使用noreload标志启动server即可避免ready方法执行两次
            print("industry app ready")
            flag = False
            try:
                flag = getattr(settings, industry_name_association_flag_string, False)
            except:
                # 如果未设置,则设置为False
                setattr(settings, industry_name_association_flag_string, False)
            finally:
                if not flag:
                    # https://docs.djangoproject.com/zh-hans/4.2/ref/applications/

                    GbIndustry = self.get_model("GbIndustry")
                    self.industry_names_obj = GbIndustry.objects.values("name").all()
                    self.init_index_proxy()
                    self.init_trie_tree()

    def init_trie_tree(self):
        start_time = time.time()
        trie = TrieTree()
        for name in self.industry_names_obj:
            trie.insert(name.get("name"))
        setattr(settings, "industry_name_association_trie", trie)
        end_time = time.time()
        print("time cost: ", end_time - start_time)
        print(f"trie树初始化完成！Cost: {end_time - start_time}")
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
        for name in self.industry_names_obj:
            index_proxy.process(name.get("name"))
        index_proxy.persist.index_construction_trigger()
        setattr(settings, "industry_name_association_index_proxy", index_proxy)
        end_time = time.time()
        print("time cost: ", end_time - start_time)
        print(f"倒排索引初始化完成！Cost: {end_time - start_time}")




