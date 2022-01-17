from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from polls.models import UserPoll, Poll

class Test_case_1(APITestCase):
    def test_1(self):
        url = reverse('start_poll')
        count = UserPoll.objects.count()
        PollInst=Poll(name="qwerty", end_date="2022-10-10", description="PollInst")
        PollInst.save()
        data = {'poll': PollInst.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserPoll.objects.count() - count, 1)
        self.assertEqual(UserPoll.objects.get().poll.id, data['poll'])
        


if __name__ == '__main__':
    unittest.main()
