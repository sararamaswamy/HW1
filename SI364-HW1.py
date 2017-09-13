## HW 1
## SI 364 F17
## Due: September 19, 2017
## 500 points
import requests
import re
import json
from bs4 import BeautifulSoup

## PART 1 - 100 points

## First, set up a new-to-this-assignment conda environment. To the Canvas assignment, you should submit:
# - A screenshot showing your environment activated and deactivated. You should feel comfortable activating and deactivating a virtual environment. ## NOTE: (You can call the env whatever you want, but remember you'll have to type it a lot and we will have to see it. It's not like a password -- consider it public.)
# - A screenshot showing the result of typing conda list at the prompt when the environment is activated. 

######

## We would not be setting up a virtual environment to run this application, and instead would use the flask package that comes with anaconda3.
## To run this application, cd to the folder containing this application
## First type into terminal export FLASK_APP=SI364-HW1.py
## If you are on Windows you need to use set instead of export.
## Next, type : python -m flask run

# [PROBLEM 1] - 150 points
# Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world!!'

@app.route('/class')
def aclass():
   return('Welcome to SI 364!')

## how do I make class a part of the url if it is a key word? 


if __name__ == '__main__':
    app.run()


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should seesomething like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:
# movie_name = "xyzrfij"
# baseurl = "https://itunes.apple.com/search" ## needed quotes around this url
# param_dic = {}
# params = {"entity":"movie", "term": movie_name}
# r = requests.get(baseurl, params)
# result_diction = json.loads(r.text) 
# print(json.dumps(result_diction, indent = 2))


@app.route('/movie/<moviename>')
def moviename(moviename):
	movie_name = moviename
	baseurl = "https://itunes.apple.com/search" ## needed quotes around this url
	param_dic = {}
	params = {"entity":"movie", "term": movie_name}
	r = requests.get(baseurl, params)
	result_diction = json.loads(r.text) 
	data_return = json.dumps(result_diction, indent = 2)
	return(data_return)
 
# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!
