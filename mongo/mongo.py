
from urllib.parse import quote
import time
import pymongo
import requests
from pymongo import MongoClient
import os
cred = quote(os.environ.get("MONGO_PWD"))
cluster_id='mongodb+srv://<user>:'+cred+'@cluster0-8j6bd.mongodb.net/test?retryWrites=true&w=majority'
cluster=MongoClient(cluster_id)
db=cluster['testBase']
collection=db['testCollection']
import short_url

inserted_list=[
{"_id":1,"url":"partnerlocation"},
{"_id":2,"url":"asim"},
{"_id":3,"url":"partner"},
{"_id":4,"url":"partnertest"},
{"_id":5,"url":"partnerwebapp"},
{"_id":6,"url":"nitesh"},
{"_id":7,"url":"anmol"},
{"_id":8,"url":"ritu"},
{"_id":9,"url":"maps"},
{"_id":10,"url":"ashu"},
{"_id":11,"url":"fbpost"},
{"_id":12,"url":"testapp"},
{"_id":13,"url":"best_food"},
{"_id":14,"url":"bulking_food"},
{"_id":15,"url":"partnerlo"},
{"_id":15,"url":"partnerlocation1"},
{"_id":17,"url":"partnerlocation2"},
{"_id":16,"url":"partnerlocation3"}

]
collection.insert_one({"_id":89,"url":"gartner"})



class EditUrl:
    def __init__(self,id,new_url_part):
        self.id=id
        self.new_url=new_url_part
    def short(self):
        main_url_part=short_url.encode_url(self.id)
        is_not_present=EditUrl.check(self)
        if is_not_present:
            print(f"you are ready to edit url from : {main_url_part} to {self.new_url}")
            collection.insert_one({"_id":self.id,"url":self.new_url})
            print("and hence edited : ")
            print("now still you not trusted on ourselves then : ")
            result=collection.find({"_id":self.id,"url":self.new_url})
            print("posted on mongo db : ",result[0])
        else:
            print("you are not ready to use this url  : ")
            print("now we have some suggetion for you related to your fav url ")
            print("if you want then enter y")
            op=input('>> ')
            if op=='y':
                try:
                    url=f"https://api.datamuse.com/words?sp={self.new_url}&max=5"
                    r=requests.get(url)
                    suggested_list=[]
                    for i in range(1,len(r.json())):
                        result=collection.find({"url":r.json()[i]['word']})
                        if result.count()==0:
                            print(f"now suggested is {r.json()[i]['word']}")



                except Exception as exception:
                    print("Error occurs . No suggetion : ",exception)

            else:
                pass
    #this function will check wether there is the url which is alredy
    # taken return true means not taken alredy:
    def check(self):
        results=collection.find({"url":self.new_url})
        if results.count()==0:
            return True
        else:
            return False

your_url_id=int(input("entr your url iD : "))
edit_url=input("entr the url you want in place of code url : ")
my_instance=EditUrl(your_url_id,edit_url)
my_instance.short()


#collection.delete_many({})
#collection.insert_one(inserted_list[0])
#results=collection.find({})
#print(results.count())
print("done ... ")
























#print(db,collection)

# now db > connection > post (dictionary like object .)
#post={"_id":0,"name":"tim","score":5}
#collection.insert_one(post)

#post1={"_id":4,"name":"nitesh"}
#post2={"_id":5,"name":"anmol"}

#collection.insert_many([post1,post2])

#now we have to find the post with the name tim .
#name=["nitesh","anmol"]
#print("waiting .......")
#results=collection.find({"name":"anmol"})
#results=collection.find({})

#print(results.count())
'''
if results.count()==0:
    print("no query is there")


else:
    for result in results:
        print(result)
'''





#time.sleep(1)
#print("done .....")

'''

id=int(input('Enter the id you want to delete to not invite him on dinner : '))
resulter=collection.find_one({"_id":id})
print(resulter['name'],"with id : ",resulter['_id']," sorrry you are not invited . ")
result_del=collection.delete_one({"_id":resulter['_id']})
print("so now the invited list is as follows : ")
resulter_in=collection.find({})
for result in resulter_in:
    print("you are invited ",result['name'])
'''
#collection.insert_one({"_id":0,"name":"tim"})

#collection.update_one({"_id":4},{"$set":{"weight":78}})
#inc will double the value .
#collection.update_one({"_id":0},{"$inc":{"weight":78}})
#print("done ... ")

