import operator
import requests
import numpy as np
import pandas as pd
import csv


#Write classes
access_token= "<your_access_token>" #get the access token from https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=%7Bobject-id%7D%2Flikes&version=v2.11
time_wanted = "1265371201" #From what time do you want the posts to be displayed?


# function re2 fetches reactions to each post, limited to 600 here coz I've never recieved more than 600 on any post I think. 

# API feed_url gets you the posts 25 at a time (you can change this)

def re2(gimme):
    res2="https://graph.facebook.com/v2.6/"+gimme+"/reactions?limit=600&__paging_token=enc_AdAXF9uurmVoZAXBLO2BIn3Ez0sc1wUeMiv5RIKFpwaZA6fVYJdP8sntFKBMfa0hepR1yBDtZB4ahrlm6I7b0p9qGJE&access_token="+access_token
    return requests.get(res2)

#TODO - Add more comments
    
feed_url = "https://graph.facebook.com/v2.5/10152460834423273/feed?limit=25&__paging_token=enc_AdC0e5dvKoSQmXJylWG9ZCB2HOcqrn0h8aKiZAXhZAWwspwXXGbMQrctxddQsukemXMFmPC1MVhZCLW74QdPJf5Xeo7M&access_token="+access_token+"&&until="+time_wanted
cnttt = 0
def do_this(feed_url,cnttt):
    call_feed_url = requests.get(feed_url)
    #Ensuring success

    if call_feed_url.status_code == 200:
        statuses = {}
        counter = 0
        for i in call_feed_url.json()['data']:
            lis = []
            lis.append(i['id'])
            lis.append(i['created_time'])
            if 'message' in i:
                lis.append(i['message'])
            elif 'story' in i:
                lis.append(i['story'])
            statuses[counter]=lis
            counter = counter+1
    li = []
    for i in statuses.values():
        li.append(i)

#    for i in li:       
        #print(i[0],"|",i[1],"|",i[2])
    if call_feed_url.status_code == 200:
        for i in li:
            if "10152460834423273" in i[0]:
                likesval = re2(i[0])
                resp_parse = likesval.json()
                x=np.array(resp_parse)
                likes = len(x.all()["data"])
                #print(likes,i[1])
                with open('./final_set_likes_date.csv','a',newline='', encoding="utf-8") as csvfile:
                    spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(str(likes)+","+(i[1]))
        
        if cnttt <12:
            cnttt = cnttt +1
            do_this(call_feed_url.json()["paging"]["next"],cnttt)
        
cnttt = 0
do_this(feed_url,cnttt)