from django.urls import path

from internal.views import *

urlpatterns = [
    path('isDeadmanEnabled', IsDeadmanEnabledView.as_view()),
    path('startBreak', StartBreakView.as_view()),
    path('stopBreak', StopBreakView.as_view()),
    path('setNoDeadman', SetNoDeadmanView.as_view())
]
