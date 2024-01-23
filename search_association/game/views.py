from django.views import View
from django import http
from django.conf import settings
from .models import TGame
from utils import response
from utils.trie.struct_ import TrieTree


# Create your views here.

class AssociativeSearchView(View):
    def get(self, request):
        # params = requests.param_dict()
        keyword = request.GET.get("keyword")
        query_type = request.GET.get("type", '1')
        print(request.GET.get("keyword"))
        if hasattr(settings, "game_name_association_trie"):
            assert isinstance(settings.game_name_association_trie, TrieTree)
        else:
            return http.JsonResponse(status=500, data={"errmsg": "settings file has no game_name_association_trie"})
        # print(settings.game_name_association_trie.root.children)
        data = []
        if query_type == '1':
            data = settings.game_name_association_trie.startwith(keyword)
        elif query_type == '2':
            data = settings.game_name_association_index_proxy.search_word_with_suggest(keyword)

        return http.JsonResponse(data=response.make_success_response(data=sorted(data, key=len)),
                                 json_dumps_params={'ensure_ascii': False})
