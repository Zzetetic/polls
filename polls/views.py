from django.contrib.sessions.backends.db import SessionStore

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll, Question, PossibleAnswer, Answer
from . import serializers


class StartPoll(APIView):
    #ограничение по ссесии
    def post(self, request, format=None):
        #если пользователь зарегистрированный проверяем возможность создать опрос если опрос не создан создаем его
        #если пользователь анонимный проверяем его сесию если он не создавал ещё то создаем
        #здесь можно ограничит по ip и по другм различным методам
        UserPollSerializerInst = serializers.UserPollSerializer(data=request.data)
        if UserPollSerializerInst.is_valid():
            UserPollSerializerInst.save()
            return Response(UserPollSerializerInst.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FinishPoll(APIView):
    #разрешение на уровне объекта
    def post(self, request, format=None):
        '''
        получить объект начатого опроса для этого пользователя по переданому идентификатору
        изменить его состояние
        '''
        #проверяем создан ли объект и если создан проверяем создан ли он этим пользователем и если все хорошо
        #заканчиваем
        return Response(UserPollSerializerInst.data, status=status.HTTP_200_OK)
        

class AnswerRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Сериализатор ответа от пользователя.
    """
    #разрешение на уровне объекта
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer


class ActivePollsList(generics.ListAPIView):
    """
    Сериализатор объекта опроса.
    Класс объекта опроса :class:polls.model.Polls
    """
    queryset = Poll.objects.all()#TODO
    serializer_class = serializers.PollSerializer

'''
class UncomplatedUserPollList(generics.ListAPIView):
    #разрешение на уровне объекта
    queryset = Answer.objects.all()#TODO
    serializer_class = serializers.UserPollSerializer

class ComplatedUserPollList(generics.ListAPIView):
    #разрешение на уровне объекта
    queryset = Answer.objects.all()#TODO
    serializer_class = serializers.UserPollSerializer
'''

class QuestionsList(APIView):
    #разрешение на уровне объекта если прохождение опроса не начиналось пользователем то отклонить
    def get(self, request, uncompleted_poll_id, question_id):
        """
        Спросить по идентификатору опроса список вопросов из базы вопросов.
        
        """
        queryset = Question.objects.all()#TODO
        serializers.QuestionSerializer(queryset)
        return Response(serializer.data)



class GetSession(APIView):
    def post(self, request, format=None):
        if request.session.session_key is None:
            request.session.create()
            return Response(status=status.HTTP_200_OK)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)
