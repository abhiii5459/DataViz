import csv
import collections

likes_list = []
dates_list=[]
dates_list2=[]
with open('./final_set_likes_date.csv','r',newline='') as csvfile2:
    spamwriter = csv.reader(csvfile2,delimiter=',')
    for i in spamwriter:
        likes_list.append(i[0])
        dates_list.append(i[1])
        dates_list2.append((dateutil.parser.parse(i[1]).astimezone()).isoformat())
with open('./testd.csv','w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    for  i in dates_list2:
        spamwriter.writerow(i)
with open('./testl.csv','w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    for  i in likes_list:
        spamwriter.writerow(i)
dates_list_only=[]
with open('./test_dates_only.csv','w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    for  i in dates_list2:
        spamwriter.writerow(i.split('T')[0])
        dates_list_only.append(i.split('T')[0])
counter=collections.Counter(dates_list_only)
with open('./test_dates_num_of_statuses.csv','w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    for  i in counter.keys():
        spamwriter.writerow(i)
with open('./test_likes_num_of_statuses.csv','w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    for  i in counter.keys():
        spamwriter.writerow(str(counter[i]))
