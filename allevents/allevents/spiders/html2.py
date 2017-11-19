
import urllib2


import requests



from BeautifulSoup import BeautifulSoup

url = "https://allevents.in/new%20delhi/all#"
response = requests.get(url)
# parse html
page = str(BeautifulSoup(response.content))


def getURL(page):
  
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"https://allevents.in/new%20delhi/', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

#f= open("url.txt","w+")
list1=[]
while True:
    url, n = getURL(page)
    page = page[n:]
    if url != "https://allevents.in/new%20delhi/all":
       # print url
	#f.write(url +"\n")
	list1.append(url)
    else:
        break
	f.close()
# fetch urls



#count=0
#with open ('url.txt','rb') as f:
 #   for line in f:
  #      count+=1

# print count
	
   
#for i, line in range(count):
 #  print i
        
#f.close()

#print (list1)

print len(list1)

print list1[:]



 	#print soup.text
	#soup = BeautifulSoup(urllib2.urlopen(x))
	#print soup.title.text
	
	#for i in soup.select('div.map-address'):
	#print(i.string)
