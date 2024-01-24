# @Author: weirdgiser
# @Time: 2024/1/24
# @Function:
from . import views
from django.urls import path

urlpatterns = [
    # 搜索联想接口
    path('associative_search/', views.AssociativeSearchView.as_view()),
]
