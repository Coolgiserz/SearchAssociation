import os
import time

from django.apps import AppConfig
from django.conf import settings
from utils.index.indexers import SimpleIndexProxy
from utils.index.persist.db import RedisIndexPersist

class MuseumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'museum'
    index_proxy_museum_name = 'museum_name_association_proxy'
    index_proxy_antique_name = 'antique_name_association_proxy'

    def ready(self):
        if os.environ.get("RUN_MAIN"):
            # 无需使用noreload标志启动server即可避免ready方法执行两次
            print("museum app ready")
            self.init_museum_proxy()
            # self.init_antique_proxy()
            # https://docs.djangoproject.com/zh-hans/4.2/ref/applications/

    def init_museum_proxy(self):
        start_time = time.time()

        GbIndustry = self.get_model("Museum")
        self.names_obj = GbIndustry.objects.values_list("instname", flat=True).all()
        setattr(settings, MuseumConfig.index_proxy_museum_name,
                SimpleIndexProxy.init_index_proxy_from_words(self.names_obj, persist_class=RedisIndexPersist(), from_scratch=False))
        end_time = time.time()

        print(f"完成, COST: {end_time - start_time}")

    def init_antique_proxy(self):
        start_time = time.time()

        GbIndustry = self.get_model("Antique")
        self.names_obj = GbIndustry.objects.values_list("antiquename", flat=True)[:200000]
        setattr(settings, MuseumConfig.index_proxy_antique_name,
                SimpleIndexProxy.init_index_proxy_from_words(self.names_obj))
        end_time = time.time()

        print(f"完成Antique, COST: {end_time - start_time}")

