import requests 
import json
from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__, template_folder=os.path.join(os.pardir, "templates"))
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://homeowner:home123@localhost:5432/homethings"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


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
    return render_template("index.html",datas=json_data["data"]["listPosts"]["posts"])
