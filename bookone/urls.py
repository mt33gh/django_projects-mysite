from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='bookone'

urlpatterns = [
    path('', TemplateView.as_view(template_name='bookone/main.html'), name='main'),
    path('list', views.MainView.as_view(), name='all_list'),
    path('list/book/create/', views.BookCreate.as_view(), name='book_create'),
    path('list/lang/create/', views.LangCreate.as_view(), name='lang_create'),
    path('list/ins/create/', views.InsCreate.as_view(), name='ins_create'),
    path('list/book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('list/lang/<int:pk>/update/', views.LangUpdate.as_view(), name='lang_update'),
    path('list/ins/<int:pk>/update/', views.InsUpdate.as_view(), name='ins_update'),
    path('list/book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('list/lang/<int:pk>/delete/', views.LangDelete.as_view(), name='lang_delete'),
    path('list/ins/<int:pk>/delete/', views.InsDelete.as_view(), name='ins_delete'),
]
