from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    '''
    Представляет строку из таблицы "Poll" из базы данных
    в ней хранятся опросы. Опросы это сущность представляющая из себя
    набор вопросов, в определенный период времени любой пользователь системы может пройти такой опрос.
    '''
    name = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField()

class UserPoll(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)
    #class Meta:
    #   unique_together = (('user', 'poll'),)
    
class Question(models.Model):
    '''
    Представляет строку из таблицы "Question" из базы данных
    в ней хранятся тестовые вопросы. В каждом опросе может присутствовать множество вопросов.
    Объекты этого класса представляют такие вопросы.
    '''
    class AnswerType(models.TextChoices):
        OPTION = "текст"
        TEXT =  "выбор варианта"
    
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)    
    text = models.TextField()
    question_type = models.CharField(max_length=255, choices=AnswerType.choices)
    
        
    

class PossibleAnswer(models.Model):
    '''
    Представляет строку из таблицы "PossibleAnswer" из базы данных
    в ней хранятся варианты ответов на вопросы из таблицы "Question"
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    value = models.CharField(max_length=255)
    correct = models.BooleanField()
    
    


class PassedPoll(models.Model):
    '''
    Представляет строку из таблицы "PassedPoll" из базы данных
    в ней хранятся пройденные опросы каждым пользователем. Для простоты в этой таблице хранятся значение полей из таблицы "Question".
    Так как в любой момент значения из "Question" могут изменится администратором.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    end_date = models.DateField()


class Answer(models.Model):
    '''
    Представляет строку из таблицы "Answer" из базы данных
    в ней хранятся выбранные каждым пользователем ответы на вопросы.
    Так как в любой момент значения из "PossibleAnswer" могут изменится администратором таблица Answer ассоциирована 
    с PassedPoll, для этого же в эту таблицу сохраняются именно значения 
    указанные пользователем а не ссылки на PossibleAnswer в случае вопросов которые имеют варианты ответов.
    '''
    passed_poll = models.ForeignKey(PassedPoll, on_delete=models.CASCADE)
    value = models.TextField() 




