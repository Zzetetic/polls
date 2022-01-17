"""polls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    #полученить сессию
    path('get-session/', views.GetSession.as_view(), name='get_session'),
    #получение списка активных опросов
    path('active-polls/', views.ActivePollsList.as_view()),
    #начать прохождение активного опроса.
    path('start-poll/', views.StartPoll.as_view(), name='start_poll'),
    #закончить прохождение опроса.
    path('finish-poll/', views.FinishPoll.as_view()),
    #получить список вопросов по начатому опросу
    path('poll/<uncompleted_poll_id>/questions', views.QuestionsList.as_view()),
    #получение списка не законченных опросов.
    #path('uncompleted-polls/', views.UncomplatedUserPollList.as_view()),
    #получение списка законченных опросов.
    #path('completed-polls/',  views.ComplatedUserPollList.as_view()),
    #получение или установка значения ответа на вопрос конкретного опроса.
    path('answer/<uncompleted_poll_id>/<question_id>', views.AnswerRetrieveUpdate.as_view()),
]
