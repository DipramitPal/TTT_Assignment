# import requests 

# response = requests.get("http://terriblytinytales.com/test.txt")
# print(response.content)
# import urllib2
from urllib.request import urlopen
from flask import jsonify
from flask import Flask, render_template
from flask import request
from flask_cors import CORS, cross_origin
_name_ = '_main_'
app = Flask(_name_)
CORS(app)

@app.route("/",methods=["GET"])
def index():
    # ran = random.rand()
    return render_template("index.html")

@app.route('/words',methods = ['POST'])
def show_list():
	print (request.headers)
	# sys.exit()
	content = request.get_json()
	try:
		limit = int(content['count'])
	except KeyError:
		limit = 0
	txt = urlopen("http://terriblytinytales.com/test.txt").read()
	txt = txt.split()
	frequency = {}
	for word in txt:
		word = word.lower()
		count = frequency.get(word,0)
		frequency[word] = count +1

	words_list = frequency.keys()
	frequency_list = []
	for words in words_list:
		temp = {}
		temp['wordName'] = words
		temp['count'] = frequency[words]
		frequency_list.append(temp)
	sorted_list = sorted(frequency_list,key=lambda words: words['count'],reverse=True)
	return json.dumps(list(sorted_list[:limit]))

	
# print(frequency)