import os
from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, Date, MetaData
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

from markupsafe import escape
from donees import api_data

app = Flask(__name__)
app.config['DEBUG'] = True

# ======= DB ======= 
db_string = "postgresql://my_user:my_password@localhost:5432/mysuperwebsitedb"
# db = SQLAlchemy(app)
db = create_engine(db_string)
migrate = Migrate(app, db)
base = declarative_base()

class Projet(base):
    __tablename__ = 'projets'
    id_projet = Column(Integer, primary_key=True)
    title = Column(String)
    slug = Column(String)
    content = Column(String)
    img_path = Column(String)
    date = Column(Date, default=datetime.now)

    def __repr__(self):
        return f"<Article[{self.id}] {self.titre}>"

class Article(base):
    __tablename__ = 'articles'
    id_article = Column(Integer, primary_key=True)
    title = Column(String)
    slug = Column(String)
    content = Column(String)
    date = Column(Date, default=datetime.now)

Session = sessionmaker(db)  
session = Session()
base.metadata.create_all(db)

# # Delete
# session.delete(doctor_strange)  
# session.commit()  



N_PROJETS = 30
N_ARTICLES = 2
UPLOAD_FOLDER = "static/images"

@app.route("/")
def accueil():
    projets = session.query(Projet) 
    articles = session.query(Article) 

    return render_template("index.html", projets=projets[:N_PROJETS], articles=articles[:N_ARTICLES])

# ======= API =======
@app.route("/api/")
@app.route("/api/<string:slug>")
def api(slug=None):
    if slug:
        escaped_slug = escape(slug)
        return api_data[escaped_slug] if escaped_slug in api_data else {"erreur": "Non exitant"}
    template = ""
    for name in api_data:
        template += f'<li><a href="/api/{name}">{name}</a></li>'
    return f"<h1>API</h1><ul>{template}</ul>"

# ======= Projets ======= 
@app.route("/projets/")
@app.route("/projets/<string:slug>")
def projets(slug=None):
    projets = session.query(Projet) 
    if slug:
        for p in projets:
            if escape(slug) == p.slug:
                return render_template("projet.html", projet=p)
    return render_template("projets.html", projets=projets)

@app.route("/projets/create", methods=["GET", "POST"])
def projet_create():
    if request.method == "POST":
        title = request.form['projet_title']
        slug = request.form['projet_slug']
        projet = request.form['projet']
        projet_image = request.files['projet_image']
        image_url = f"/static/images/thumb_large.png"
        if projet_image.filename != "":
            image_url = f"/static/images/{projet_image.filename}"
            projet_image.save(os.path.join(UPLOAD_FOLDER, projet_image.filename))
        #insert in database
        new_project = Projet(title=title, slug=slug, content=projet, img_path=image_url)  
        session.add(new_project)  
        session.commit()
        return redirect(url_for("projets")) 
        
    return render_template("projet_create.html")

# ======= Articles ======= 
@app.route("/articles/")
@app.route("/articles/<string:slug>")
def articles(slug=None):
    articles = session.query(Article)
    if slug:
        for a in articles:
            if escape(slug) == a.slug:
                return render_template("article.html", article=a)
    return render_template("articles.html", articles=articles)

@app.route("/articles/create", methods=["GET", "POST"])
def article_create():
    if request.method == "POST":
        title = request.form['article_title']
        slug = request.form['article_slug']
        article = request.form['article']
        new_article = Article(title=title, slug=slug, content=article)  
        session.add(new_article)  
        session.commit()
        return redirect(url_for("articles")) 
        
    return render_template("article_create.html")

# ======= Login =======
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return "<h1>utilisateur connecte</h1>"
    return render_template("login.html")

@app.errorhandler(404)
def page_404(error):
    return render_template('404.html'), 404