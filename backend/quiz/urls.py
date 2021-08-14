from django.urls import path

from .views import GenerateQuestion

app_name = 'quiz'

urlpatterns = [
    path('question', GenerateQuestion.as_view(), name='generate_question'),
]