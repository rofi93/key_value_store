from django.urls import path
from .views import KeyValueStoreView

urlpatterns = [
    path('values/', KeyValueStoreView.as_view(), name='values')
]
