from flask import Flask, render_template
from newsapi import NewsApiClient

from  email_reader import  mess_read


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/ham')
def Index():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    sub1,to1,from1,date1,desc1=mess_read()


    desc1.reverse()
    sub1.reverse()
    to1.reverse()
    from1.reverse()
    date1.reverse()


  #  for i in range(len(articles)):
  #      myarticles = articles[i]


 #       news.append(myarticles['title'])
  #      desc.append(myarticles['description'])
  #      img.append(myarticles['urlToImage'])



    mylist = zip(sub1,to1,from1,date1,desc1)


    return render_template('index.html', context = mylist)



@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    sub1,to1,from1,date1,desc1=mess_read()


    desc1.reverse()
    sub1.reverse()
    to1.reverse()
    from1.reverse()
    date1.reverse()


  #  for i in range(len(articles)):
  #      myarticles = articles[i]


 #       news.append(myarticles['title'])
  #      desc.append(myarticles['description'])
  #      img.append(myarticles['urlToImage'])



    mylist = zip(sub1,to1,from1,date1,desc1)


    return render_template('bbc.html', context = mylist)


if __name__ == "__main__":
    app.run(debug=True)