from django.contrib import admin
from django.urls import path
from .views import NewsListView, NordMiniView, NordGSMView, NordGSMMetalView, NordGSMAirView, CatalogView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("news", NewsListView.as_view(), name="news"),
    path("", HomeView.as_view(), name="index"),
    path("nord-gsm", NordGSMView.as_view(), name="nord-gsm"),
    path("nord-mini", NordMiniView.as_view(), name="nord-mini"),
    path("nord-gsm-metal", NordGSMMetalView.as_view(), name="nord-gsm-metal"),
    path("nord-gsm-air", NordGSMAirView.as_view(), name="nord-gsm-air"),
    path("catalog", CatalogView.as_view(), name="catalog"),
]