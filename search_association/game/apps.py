import os
# django.setup()
from django.apps import AppConfig
from django.conf import settings
from utils.trie.struct_ import TrieTree

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
        print("初始化联想算法...")

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
                    game_names_obj = TGame.objects.values("name_zh").all()
                    tree = TrieTree()
                    for name in game_names_obj:
                        tree.insert(name.get("name_zh"))
                    setattr(settings, "game_name_association_trie", tree)

                    print("联想算法初始化完成！")





