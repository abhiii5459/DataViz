scrapy shell "http://192.168.1.4:8083/html/timeline.htm"
li2 = response.css("div.meta::text").extract()

with open('newxl.csv','w') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
    wr.writerow(li2)
