import requests 
import json
from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    render_template,
    url_for,
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from api.forms.create import PostCreateForm
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__, template_folder=os.path.join(os.pardir, "templates"))
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://homeowner:home123@localhost:5432/homethings"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()
# csrf.init_app(app)


@app.route("/")
def hello():
    url = "http://localhost:5000/graphql"

    body = """ 
        { 
        listPosts {
            success
            errors
            posts {
            id
            title 
            description
            created_at
            updated_at
            }
        }
        } 
        """
    response = requests.post(url=url, json={"query": body})
    json_data = response.json()

    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.status_code)
    # return json_data["data"]["listPosts"]['posts']
    return render_template("list.html",datas=json_data["data"]["listPosts"]["posts"])


@app.route("/list")
def list():
    url = "http://localhost:5000/graphql"

    body = """ 
        { 
        listPosts {
            success
            errors
            posts {
            id
            title 
            description
            created_at
            }
        }
        } 
        """
    response = requests.post(url=url, json={"query": body})
    json_data = response.json()

    # print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.status_code)
    # return json_data["data"]["listPosts"]['posts']
    return render_template("list.html", datas=json_data["data"]["listPosts"]["posts"])


@app.route("/create", methods=["GET", "POST"])
def create():
    form = PostCreateForm()
    if form.validate_on_submit():
        # post = post(form.title.data, form.description.data)

        url = "http://localhost:5000/graphql"

        # Construct the GraphQL mutation
        query = """
        mutation createPost {
            createPost(
                title: "%s", 
                description: "%s"
            ) {
                post {
                    id
                    title
                    description
                }
                success
                errors
            }
        }
        """ % (
            form.title.data,
            form.description.data,
        )
        response = requests.post(url=url, json={"query": query})
        json_data = response.json()

        print("response status code: ", response.status_code)
        if response.status_code == 200:
            flash("Saved successfully")
            return redirect(url_for("create"))
            print("response : ", response.status_code)
        # return json_data["data"]["listPosts"]['posts']
    return render_template("create.html", form=form)


@app.route("/update")
def update():
    url = "http://localhost:5000/graphql"

    body = """ 
        { 
        listPosts {
            success
            errors
            posts {
            id
            title 
            description
            created_at
            }
        }
        } 
        """
    response = requests.post(url=url, json={"query": body})
    json_data = response.json()

    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", json_data["data"]["listPosts"]["posts"])
    # return json_data["data"]["listPosts"]['posts']
    return render_template("index.html", datas=json_data["data"]["listPosts"]["posts"])
