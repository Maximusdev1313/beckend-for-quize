from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('class', ClassViewSet)
router.register('quiz', QuizViewSet)
router.register('condition', ConditionViewSet)
router.register('variant', VariantViewSet)
# router.register('simple', SimpleFilesViewSet)

urlpatterns = [
    path('', include(router.urls) ),
]