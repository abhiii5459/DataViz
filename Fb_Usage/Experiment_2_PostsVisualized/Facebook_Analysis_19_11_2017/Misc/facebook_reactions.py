import operator
import requests

feed_url = "https://graph.facebook.com/v2.5/10152460834423273/feed?limit=100&__paging_token=enc_AdC0e5dvKoSQmXJylWG9ZCB2HOcqrn0h8aKiZAXhZAWwspwXXGbMQrctxddQsukemXMFmPC1MVhZCLW74QdPJf5Xeo7M&since=1510280679&access_token=EAACEdEose0cBADamPVA31qDpt8h4aHFwCMLnZB8i1BootdvmP54SqkPE5GZARzpIMWUIHXzEEznZBBS8zsf32ZCzN0UBW5MNs2AYZBp3ZAHb3jfGQy1I1lW4783JJuY6LtlZAZBpiNge1bXAFJZArtxbsLj3NiIGVtNS02yg3QfcqvrwZASeN0aTx5ZAHGeocpMvxkZD"
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

for i in li:
    print(i[0],"|",i[1],"|",i[2])