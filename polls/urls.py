from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import views

admin.site.site_header = "Polls Application Administration"

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('api/', include(router.urls)),
]
