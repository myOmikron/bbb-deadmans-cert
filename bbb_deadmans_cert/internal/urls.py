from django.urls import path

from internal.views import *

urlpatterns = [
    path('isDeadmanEnabled', IsDeadmanEnabledView.as_view())
]