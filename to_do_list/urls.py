from django.urls import path

from to_do_list.views.base import index_view
from to_do_list.views.tasks import add_view, detail_view, delete_view

urlpatterns = [
    path('', index_view),
    path('task/add', add_view),
    path('task/', detail_view),
    path('task/delete/', delete_view),
]
