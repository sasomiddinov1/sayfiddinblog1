from django.urls import path
from .views import HomaPageView

urlpatterns = [
    path('', HomaPageView.as_view(), name='home'),
]