from django.urls import path, include
from rest_framework import routers
from. import views

router = routers.DefaultRouter()
router.register("scraping_tasks", views.ScrapingTaskViewSet, basename="scraping_tasks")

urlpatterns = [
    path("", include(router.urls)),
    path("start_scraping/", views.StartScrapingAPIView.as_view()),
    path("scraping_status/<int:job_id>/", views.ScrapingStatusAPIView.as_view()),
]