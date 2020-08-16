#pub sub


import redis
import os, sys
from django.core.wsgi import get_wsgi_application
proj_path = "/"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webcastsite.settings")
sys.path.append(proj_path)
# This is so my local_settings.py gets loaded.
os.chdir(proj_path)
# This is so models get loaded.
application = get_wsgi_application()
from magazine.models import Magazines

'''
(1) : first of all whenever admin create a new web cast
      then all the subscribers of that maga got the 
      notification that new web cast info is reach to user.


'''
test_db = 5


class Subscribed_user:
    def __init__(self, username, channel_name):
        self.r = redis.Redis(db=test_db)
        self.p = self.r.pubsub()
        self.p.subscribe(channel_name)
        self.p.get_message()

    def message(self):
        return self.p.get_message()['data'].decode('utf-8')



class Message:
    def __init__(self, msg, chanel_name):
        self.msg = msg
        self.channel_name = chanel_name
        r = redis.Redis(db=test_db)

        r.publish(chanel_name, self.msg)
        # channel sent the message


class Notifiy:

    def __init__(self, channel_name):

        self.channel_name = channel_name
        # getting all the subscribers list.
        magazine = Magazines.objects.get(name=channel_name)
        users = magazine.subscribed_user.all()
        userslis = []
        for user in users:
            userslis.append(user.__str__())
        # users are the subscribed user
        print(userslis)
        u=[]
        messages={}
        for user in userslis:
            u.append(Subscribed_user(user,channel_name))
        message = Message("hello my subscribers to my latest casts .",channel_name)
        for i in range(len(u)):
            l=u[i].message()
            messages[userslis[i]]=l

        print(messages)


new_notification = Notifiy("workouts")





