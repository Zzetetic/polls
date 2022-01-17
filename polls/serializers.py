from rest_framework import serializers, generics
from .models import Poll, Question, PossibleAnswer, Answer, UserPoll

class PollSerializer(serializers.ModelSerializer):
    """
    Сериализатор объекта опроса.
    """
    class Meta:
        model = Poll
        fields = '__all__'



class UserPollSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = UserPoll
        fields = '__all__'


class AnswerSerializer(generics.CreateAPIView):
    """
    Сериализатор ответа от пользователя.
    """
    class Meta:
        model = Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'



class PossibleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossibleAnswer
        fields = '__all__'
