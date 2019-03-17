import bs4 as bs
import urllib.request

#from PyQt5.QtWidgets import QApplication
#from PyQt5.QtCore import QUrl
#from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage

from urllib.request import urlopen as uReq,Request
from bs4 import BeautifulSoup as soup
import pyrebase
config = {
    "apiKey": "AIzaSyDQwk60FvDVYKJN-Cy3xPKulLrRdYCZT8M",
    "authDomain": "pichkari2.firebaseapp.com",
    "databaseURL": "https://pichkari2.firebaseio.com",
    "projectId": "pichkari2",
    "storageBucket": "pichkari2.appspot.com",
    "messagingSenderId": "482691617687"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


req = Request('https://economictimes.indiatimes.com/markets/bonds', headers={'User-Agent': 'Mozilla/5.0'})
sauce = uReq(req).read()

soup = bs.BeautifulSoup(sauce ,'lxml')

mydivs = soup.find("div", {"class": "tabdata"})
#print(mydivs)
champak = mydivs.find_all('div',{'class':'eachStory'})
'''
for paragraph in champak:
    r = paragraph.find('h3')
    
    print(r.text)
'''
i = 0
loop = 1
popo = "link"

for paragraph in soup.find_all('div',{'class':'eachStory'}):
    g = paragraph.find('h3')
    #c = paragraph.find('p')
    tym = paragraph.find('time')
    img = paragraph.find('img')
    img_url = img['data-original']
            
    #print(g.text)
    #print(c.text)
    #print(tym.text)
    #print("Image url-->",img_url)
    loop+=1
    if( loop == 18):    #for 10 news
        break
    r = paragraph.find('a')
    urlo = r.get('href')
    urlo = 'https://economictimes.indiatimes.com'+urlo
    #print("-->",urlo)
    i+=1
    popo+=str(i)
    #print("+++>",popo)
    #remove last character of the string
    db.child(popo+'/name').update({"name":urlo})
    db.child(popo+'/date').update({"value":tym.text})
    db.child(popo+'/image').update({"value":img_url})
    #db.child(popo+'/paragraph').update({"value":c.text})            
    db.child(popo+'/heading').update({"value":g.text})            

    req = Request(urlo, headers={'User-Agent': 'Mozilla/5.0'})
    sauce2 = uReq(req).read()

    soup2 = bs.BeautifulSoup(sauce2 ,'lxml')
    for paragraph in soup2.find_all('div',{'class':'artText'}):
        para = paragraph.find('div',{'class':'Normal'})
        db.child(popo+'/paragraph').update({"value":para.text})
        title = para.text.split('.',1)
        #print(para.text)
        print('Title:',title[0])
        db.child(popo+'/title').update({"value":title[0]})
    
        
    popo = ''.join([i for i in popo if not i.isdigit()])
    
