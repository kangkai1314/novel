#some useful function for scrapy
def writeResponse(crawler,response):
    print(crawler.name)
    with open('%s.html'%(crawler.name),'w') as f:
        f.write(response.body)