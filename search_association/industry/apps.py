import os
from django.apps import AppConfig
from django.conf import settings
from utils.trie.struct_ import TrieTree

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
                    TGame = self.get_model("GbIndustry")
                    industry_names_obj = TGame.objects.values("name").all()
                    tree = TrieTree()
                    for name in industry_names_obj:
                        tree.insert(name.get("name"))
                    setattr(settings, "industry_name_association_trie", tree)
                    print("联想算法初始化完成！")




