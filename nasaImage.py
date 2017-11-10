from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def home():
	u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=0XyeqBRNTN0NQCOWgHjq7K9GH6OAXJZoYjN7uE8Q")
	jsonString = u.read()
	d = json.loads(jsonString)
	return render_template("nasaimg.html", img = d["hdurl"], desc = d["explanation"], date = d["date"])

if __name__ == "__main__":
	app.debug = True
	app.run()
