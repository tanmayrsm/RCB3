import bs4 as bs
import urllib.request
from gensim.summarization import summarize
import nltk
from textblob import TextBlob
        

from urllib.request import urlopen as uReq,Request
from bs4 import BeautifulSoup as soup
import pyrebase
config = {
    "apiKey": "AIzaSyBsU8Y4TbAIyu8GsRDuZyTzw0_37eke1nY",
    "authDomain": "pichkari-118b9.firebaseapp.com",
    "databaseURL": "https://pichkari-118b9.firebaseio.com",
    "projectId": "pichkari-118b9",
    "storageBucket": "pichkari-118b9.appspot.com",
    "messagingSenderId": "908054057055"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()







sauce = urllib.request.urlopen('https://in.reuters.com/news/archive/bondNews').read()

soup = bs.BeautifulSoup(sauce ,'lxml')

i = 0
loop = 1
popo = "link"
#print(soup.title.string)
for image in soup.find_all('div',{'class' : 'story-photo lazy-photo '}):
    loop+=1
    if( loop == 12):    #for 10 news
        break
    r = image.find('a')
    urlo = r.get('href')
    #print('image:',r)
    img = r.find('img')
    img_url = img['org-src']
    #print(img_url,"  img")
    
    i+=1
    popo+=str(i)
    #print("popo:",popo)
    if img_url!=None:
        db.child(popo+'/image').update({"value":img_url})
    popo = ''.join([i for i in popo if not i.isdigit()])
    
i = 0
loop = 1
popo = "link"    
for paragraph in soup.find_all('div',{'class':'story-content'}):
    loop+=1
    if( loop == 12):    #for 10 news
        break
    r = paragraph.find('a')
    urlo = r.get('href')
    urlo = 'https://www.reuters.com'+urlo
    #print(urlo)
    i+=1
    popo+=str(i)

    #find date of post
    tym = paragraph.find('time')
    tym = tym.text
    tym = tym.replace("\r","")
    tym = tym.replace("\n","")
    db.child(popo+'/name').update({"name":urlo})
    db.child(popo+'/date').update({"value":tym})

    

    #uss urlo ke andar jao...then h1 and para ko nikalke link1 ke contents me daalo
    #crawler level 1
    sauce2 = urllib.request.urlopen(urlo).read()
    soup2 = bs.BeautifulSoup(sauce2 ,'lxml')
    for paragraph in soup2.find_all('div',{'class':'StandardArticle_inner-container'}):
        heading = paragraph.find('h1')
        img = paragraph.find('div',{'class':'LazyImage_container'})
            
        db.child(popo+'/heading').update({"value":heading.text})
        paru = paragraph.find('div',{'class':'StandardArticleBody_body'})
        final_para=""
        for palak in paru.find_all('p'):
            final_para=final_para + palak.text
        #print(final_para)
        db.child(popo+'/paragraph').update({"value":final_para})

        ################
        text = final_para
        print ( "Summary:__________________",summarize(text) )

        db.child(popo+'/summary').update({"value":summarize(text)})

        

        blob1 = TextBlob(summarize(text))
        print(format(blob1.sentiment))
        
        db.child(popo+'/polarity').update({"value":blob1.sentiment[0]})
        db.child(popo+'/subjective').update({"value":blob1.sentiment[1]})

        
        ###############

        
        #print(heading.text)


        title = heading.text.split('.',1)
        #print(para.text)
        print('Title:',title[0])
        db.child(popo+'/title').update({"value":title[0]})
    
        
  #  print(tym)
    
    #remove last character of the string
    popo = ''.join([i for i in popo if not i.isdigit()])
    
