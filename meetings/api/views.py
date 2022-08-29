from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework import status
from meetings.models import Meetings
from .serializer import MeetingSerializer
import jwt
import datetime
import requests
import json
from rest_framework.response import Response




class MeeetingsCreateAPIView(CreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingSerializer

    def perform_create(self, serializer):
        topic = self.request.POST['topic']
        starttime = self.request.POST['starttime']
        duration = self.request.POST['duration']
        password = self.request.POST['passwords']
        
        time_now = datetime.datetime.now()
        expiration_time = time_now+datetime.timedelta(seconds=20)
        rounded_off_exp_time = round(expiration_time.timestamp())
        headers = {'alg':"HS256","typ":"JWT"}
        payload = {'iss':"zflt_IuySqaHMH0ZLLnVPA","exp":rounded_off_exp_time}
        encoded_jwt = jwt.encode(payload, "n1Y9WDJNOcpRaQC0NguycCPzz316tBMJZhSd", algorithm="HS256") 
        email = "surent.calcgen@gmail.com"
        url = 'https://api.zoom.us/v2/users/{}/meetings'.format(email)
        date = datetime.datetime(2021,7,5,13,30).strftime("%Y-%m-%dT%H:%M:%SZ")
        header = {"authorization":"Bearer {}".format(encoded_jwt)}
        obj = {"topic":topic, "starttime":starttime, "duration":duration,'password':password}
        create_meeting = requests.post(url,json=obj,headers=header)     
        serializer.save(url=create_meeting.text)


class MeetingListApi(ListAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingSerializer
