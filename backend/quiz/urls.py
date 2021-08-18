from django.urls import path

from .views import GenerateQuestion, PracticeQuestion

app_name = 'quiz'

urlpatterns = [
    path('question', GenerateQuestion.as_view(), name='generate_question'),
    path('practice', PracticeQuestion.as_view(), name='practice_question')
]