# crypto_app/urls.py

from django.urls import path
from .views import StartScrapingView, ScrapingStatusView

urlpatterns = [
    path('taskmanager/start_scraping/', StartScrapingView.as_view(), name='start-scraping'),
    path('taskmanager/scraping_status/<str:job_id>/', ScrapingStatusView.as_view(), name='scraping-status'),
]
# crypto_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('crypto_app.urls')),
]
