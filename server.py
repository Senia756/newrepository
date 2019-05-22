from bottle import route, run, view
from bottle import static_file
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies



@route("/api/forecast")

def api_forecast():

	prophecies = generate_prophecies(6,2)
	return{"prophecies": prophecies
  
}

@route("/")
@view("predictions")

def index_new():
	now = dt.now()
	return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": generate_prophecies(),
    }

@route("/new.js")
def ja_js():
    return static_file("new.js", root="static")

@route("/styles.css")
def styles():
    return static_file("styles.css", root="static")
run(
  host="localhost",
  port=8080,
  autoreload=True
)

