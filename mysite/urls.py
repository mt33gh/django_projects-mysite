"""
URL configuration for mysite project.


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

#Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path("", include("home.urls")),
    path("views/", include("views.urls")),
    path("views2/", include("views2.urls")),
    path("polls/", include("polls.urls")),
    path("polls2/", include("polls2.urls")),
    path("tmpl/", include("tmpl.urls")),
    path("route/", include("route.urls", namespace="nsroute")),
    path("gview/", include("gview.urls")),
    path("getpost/", include("getpost.urls")),
    path("session/", include("session.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("authz/", include("authz.urls")),
    path("form/", include("form.urls")),
    path("autos/", include("autos.urls")),
    path("autos2/", include("autos2.urls")),
    path("bookone/", include("bookone.urls")),
    path("myarts/", include("myarts.urls")),
    path("crispy/", include("crispy.urls")),
    path("menu/", include("menu.urls")),
    #path("bookmany/", inclulde("bookmany.urls")),    # bookmany/urls.py is not created yet.
    #path("many/", include("many.urls")),             # many/urls.py is not created yet.
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
]
