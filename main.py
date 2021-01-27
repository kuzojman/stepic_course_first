from flask import Flask, render_template, request

app = Flask(__name__)


points = [
  "951 Marsh StreetMiddleburg, FL 32068",
  "207 Westport Drive Uniondale, NY 11553",
  "1 Second AvenueWayne, NJ 07470",
]

tags = ["jazz", "blues", "rnb", "bluegrass", "lounge"]
videos = [{
    "id":1,
    "title": "Как построить открытую террасу к дому своими руками",
    "src": "http://videohost.me/hDX4hWWV5Ok.mp4",},
    {
    "id": 2,
    "title": "How To Learn Anything 10x Faster",
    "description": "Interested in learning more about Charisma University? You’re going to spend thousands and thousands hours learning over the course of your life.  What’s crazy is that despite the fact that we have all those hours sitting in the classroom, learning musical instruments, martial arts, business, language, whatever - no one teaches us how to optimize that learning experience.",
    "src": "http://videohost.me/YLwFbwPbq.mp4",
}]

for video in videos:
    print(video)

mylist = [
  "Capicola",
  "Celery Root",
  "Marjoram - Dried, Rubbed",
  "Bread - Italian Sesame Poly",
  "Cheese - Bocconcini",
  "Mushroom - Shitake, Dry",
  "French Pastry - Mini Chocolate",
]

links = [
  {"title":"Главная","link":"/"},
  {"title":"О Нас","link":"/about/"},
  {"title":"Контакты","link":"/contact/"},
]
for i in range(len(links)):
    print((links[i])["title"])

positions=[
  {
    "title":"Руководитель отдела web-разработки",
    "salary":"180 000 - 200 000",
    "level":"lead",
    "tags": ["ООП","Git","Flask","Redis","Управление проектами","Управление людьми",
             "Построение команды","Ведение переговоров"],
  },
  {
    "title":"Python Developer",
    "salary":"200 000",
    "level":"middle",
    "tags":["Python","Django","PostgreSQL","Linux","Git"],
  },
  {
    "title":"Python developer",
    "salary":"130 000 - 180 000",
    "level":"middle",
    "tags":["Django","Python","Flask","PostgreSQL","Высоконагруженные системы","Git","Docker"],
   }
]

carriers=[
  {"name": "American Airlines", "planes": 950, "founded": 1934, "passengers": 193.7},
  {"name": "Lufthansa", "planes": 351, "founded": 1955 , "passengers": 77.5},
  {"name": "Ryanair", "planes": 438, "founded": 1984,  "passengers": 66.5},
  {"name": "Southwest Airlines", "planes": 746,"founded": 1971,"passengers": 101.3},
  {"name": "Delta", "planes": "809", "founded": "1929" , "passengers": 161.1},
]



movies = [
  {
    "title":"El Camino: A Breaking Bad Movie",
    "rutitle":"Путь: Во все тяжкие. Фильм",
    "genres":["Криминальный","Драма"],
    "imdbrate":8.8,
  },
  {
    "title": "The Irishman",
    "rutitle": "Ирландец",
    "genres": ["Криминальный", "Исторический"],
    "imdbrate": 8.7,
  },
  {
    "title": "Downton Abbey",
    "rutitle": "Аббатство Даунтон",
    "genres": ["Драма"],
    "imdbrate": 8.7,
  },
  {
    "title": "Avengers Endgame",
    "rutitle": "Мстители: Финал",
    "genres": ["Приключения", "Фантастика", "Боевик"],
    "imdbrate": 8.6,
  },
  {
    "title": "Joker",
    "rutitle": "Джокер",
    "genres": ["Криминальный", "Триллер", "Драма"],
    "imdbrate": 8.7,
  },
]







@app.route('/')
def open_index_page():
    return render_template('index.html')

@app.route('/tour')
def open_tour_page():
    return render_template('tour.html')

@app.route('/departure')
def open_departure_page():
    return render_template('departure.html')

@app.route('/data')
def data_index_page():
    return render_template('data.html',
                           tags=tags,
                           videos=videos,
                           points=points,
                           mylist=mylist,
                           links=links,
                           positions=positions,
                           carriers=carriers,
                           movies=movies)


@app.route('/base_2')
def base_page():
    return render_template('base_2.html')



if __name__ == '__main__':
    app.run()

#{ % for tags_inside in {{k.tags}} %}
#< ul > {{tags_inside}} < / ul >
#{ % endfor %}