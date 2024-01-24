from django.views import View
from django import http
from django.conf import settings
from django.db.models import Q
from .apps import MuseumConfig
from .models import Museum, Antique
# Create your views here.
class AssociativeSearchView(View):
    def get(self, request):
        keyword = request.GET.get("keyword")
        query_type = request.GET.get("type", 1)
        if int(query_type) == 1:
            proxy = getattr(settings, MuseumConfig.index_proxy_museum_name)
            data = proxy.search_word_with_suggest(keyword)
            print("基于倒排索引搜索")
            return http.JsonResponse(data={"data": sorted(data, key=len), "count": len(data)}, status=200,
                                     json_dumps_params={'ensure_ascii': False})
        elif int(query_type) == 2:
            data = Museum.objects.filter(Q(instname__icontains=keyword)).values_list("instname", flat=True)
            print("基于SQL like搜索")
            return http.JsonResponse(data={"data": sorted(data, key=len), "count": len(data)}, status=200,
                                     json_dumps_params={'ensure_ascii': False})

        elif int(query_type) == 3:
            proxy = getattr(settings, MuseumConfig.index_proxy_antique_name)
            data = proxy.search_word_with_suggest(keyword)
            print("基于倒排索引搜索")
            return http.JsonResponse(data={"data": sorted(data, key=len), "count": len(data)}, status=200,
                                     json_dumps_params={'ensure_ascii': False})

        elif int(query_type) == 4:
            data = Antique.objects.filter(Q(antiquename__icontains=keyword)).values_list("antiquename", flat=True)
            print("基于SQL like搜索")
            return http.JsonResponse(data={"data": sorted(data, key=len), "count": len(data)}, status=200,
                                     json_dumps_params={'ensure_ascii': False})

