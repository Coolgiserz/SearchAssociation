from django.views import View
from django import http
from django.db.models import Q
from django.conf import settings
from .models import GbIndustry
from utils.trie.struct_ import TrieTree


# Create your views here.
# 对于行业表而言，like查询进行前缀查询可能需要几十ms，但使用trie树进行联想仅需不到5ms
def associative_search_with_trie(keyword):
    print("trie树前缀搜索")

    if hasattr(settings, "industry_name_association_trie"):
        assert isinstance(settings.industry_name_association_trie, TrieTree)
    else:
        return http.JsonResponse(status=500, data={"errmsg": "settings file has no game_name_association_trie"})
    # print(settings.game_name_association_trie.root.children)
    data = settings.industry_name_association_trie.startwith(keyword)

    return http.JsonResponse(data={"data": sorted(data, key=len)}, status=200,
                             json_dumps_params={'ensure_ascii': False})


def associative_search_with_like_query_prefix(keyword, mode=1):
    """
    基于like查询进行前缀搜索
    :param keyword:
    :return:
    """
    print("like查询前缀搜索")
    if mode == 1:
        data = GbIndustry.objects.filter(Q(name__startswith=keyword)).values_list("name", flat=True)
    else:
        data = GbIndustry.objects.filter(Q(name__icontains=keyword)).values_list("name", flat=True)
    return http.JsonResponse(data={"data": sorted(data, key=len)}, status=200,
                             json_dumps_params={'ensure_ascii': False})


class AssociativeSearchView(View):
    def get(self, request):
        print(request)
        keyword = request.GET.get("keyword")
        query_type = request.GET.get("type", 1)
        print(request.GET.get("keyword"))
        if query_type == '1':
            return associative_search_with_trie(keyword=keyword)
        elif query_type == '2':
            return associative_search_with_like_query_prefix(keyword=keyword)
        else:
            return associative_search_with_like_query_prefix(keyword=keyword, mode=2)
