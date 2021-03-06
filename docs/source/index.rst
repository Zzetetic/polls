.. Polls documentation master file, created by
   sphinx-quickstart on Mon Sep 27 17:48:46 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Polls's documentation!
=================================
Система предоставляет возможность создавать тестовые опросы и проходить их. Она работает через интернет.

Система построена с использованием архитектурного стиля REST.
Она состоит из клиентской и серверной части. Серверная часть предоставляет интерфейс построенный по принципам REST. Им можно воспользоватся с помощью подходящего для этого средства.
Например программой telnet, curl, httpie, openapi-cli и т. п. Или библиотекой для какого нибудь языка программирования, например request для языка python.

Клиентская часть работает с этим интерфейсом и предоставляет графический интерфейс. Чтобы работать через графический интерфейс необходимо воспользоватся современным браузером например таким как firefox, opera, chromium, google chrome и т. п. Браузер загрузит необходимые компоненты и предоставит графический интерфейс для работы с системой.

Серверна часть предоставляет следующий интерфейс.

* получение списка активных опросов
* начать прохождение активного опроса.
* закончить прохождние опроса.
* получение списка вопросов по начатому опросу.
* получение списка не законченных опросов.
* получение списка законченных опросов.
* отправка ответа на конкретный вопрос проходимого опроса.
* получение значения ответа, который был установлен ранее, на конкретный вопрос проходимого опроса.
* изменение значения ответа, который был установлен ранее, на конкретный вопрос проходимого опроса.

Для того чтобы начать работать с системой с помощью интерфейса предоставляемого сервером необходимо:

1. Получить список активных вопросов.
2. Выбрать подходящий.
3. Начать прохождение опроса с помощью соответвующего айпи. Сервер пришлет идентификатор начатого опроса.

В случае если имеются незаконченные опросы можно получить список незаконченных опросов с помощью интерфейса.
Далее необходимо получить список вопросов в незаконченном опросе.
И ответить на каждый, в случае если хочешь изменить ответ на какой-то вопрос, то это можно сделать.
Ответы на вопросы можно оставлять пустыми.
После того как закончил тестирование необходимо сообщить об этом системе с помощью её интерфейса.
Опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы.




.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
