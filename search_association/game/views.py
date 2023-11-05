from django.views import View
from django import http
from django.conf import settings
from .models import TGame
from utils import response
from utils.trie.struct_ import TrieTree
# Create your views here.

class AssociativeSearchView(View):
    def get(self, requests):
        keyword = requests.GET.get("keyword")
        print(requests.GET.get("keyword"))
        assert isinstance(settings.game_name_association_trie, TrieTree)
        # print(settings.game_name_association_trie.root.children)
        data = settings.game_name_association_trie.startwith(keyword)

        return http.JsonResponse(data=response.make_success_response(data=sorted(data, key=len)),
                                 json_dumps_params={'ensure_ascii': False})
