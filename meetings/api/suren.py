import jwt
import datetime
import requests
import json

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
obj = {"topic":"Test meeting", "starttime":date, "duration":30,'password':12345}
create_meeting = requests.post(url,json=obj,headers=header)
print(create_meeting.text)