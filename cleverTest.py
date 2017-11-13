from flask import Flask, render_template, request
import urllib2
import json

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirect():
	response = request.args.get("input","")
	cs = request.args.get("cs", "")
	url = 'https://www.cleverbot.com/getreply?key=CC5cuMUk-FTbz2V-XmGJTRKsAWA&input=' + response.replace(" ", "+") + '&cs=' + cs
	print url
	u = urllib2.urlopen(url)
	jsonString = u.read()
	d = json.loads(jsonString)
	return render_template("cleverTest.html", cs = d["cs"], output = d["output"])


@app.route('/', methods=['GET'])
def home():
	u = urllib2.urlopen("https://www.cleverbot.com/getreply?key=CC5cuMUk-FTbz2V-XmGJTRKsAWA&input=hello")
	jsonString = u.read()
	d = json.loads(jsonString)
	return render_template("cleverTest.html", cs = d["cs"], output = d["output"])

if __name__ == "__main__":
	app.debug = True
	app.run()
